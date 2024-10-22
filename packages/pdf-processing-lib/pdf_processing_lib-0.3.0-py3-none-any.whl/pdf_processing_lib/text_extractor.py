import os
import pandas as pd
import fitz  # PyMuPDF
from joblib import Parallel, delayed
import time
import gc 
import xml.etree.ElementTree as ET
from xml.dom import minidom
import PIL.Image

class TextExtractor:
    def __init__(self, input_directory):
        self.input_directory = input_directory

    def extract_text_from_pdf(self, pdf_path, page_num, boxes):
        doc = fitz.open(pdf_path)
        page = doc.load_page(page_num)
        texts = []
        for box in boxes:
            rect = fitz.Rect(box[:4])
            text = page.get_text("text", clip=rect)
            texts.append(text)
        doc.close()
        return texts

    def create_cvat_task_xml(self, task_name):
        root = ET.Element('annotations')
        version = ET.SubElement(root, 'version')
        version.text = '1.1'
        
        image_id = 0
        for entry in os.listdir(self.input_directory):
            pdf_output_dir = os.path.join(self.input_directory, entry)
            if os.path.isdir(pdf_output_dir) and pdf_output_dir.endswith('_output'):
                base_name = entry[:-7]  # Remove '_output' from the end
                final_dir = os.path.join(pdf_output_dir, 'final')
                original_images_dir = os.path.join(pdf_output_dir, f"{base_name}_images_original")
                
                if os.path.exists(final_dir) and os.path.exists(original_images_dir):
                    for tsv_file in sorted(os.listdir(final_dir)):
                        if tsv_file.startswith('combined_page') and tsv_file.endswith('.tsv'):
                            page_num = tsv_file.split('page')[1].split('.')[0]
                            tsv_path = os.path.join(final_dir, tsv_file)
                            df = pd.read_csv(tsv_path, sep='\t', encoding='utf-8')
                            
                            image_name = f"{base_name}_page{page_num}.jpg"
                            image_path = os.path.join(original_images_dir, image_name)
                            
                            if os.path.exists(image_path):
                                with PIL.Image.open(image_path) as img:
                                    width, height = img.size
                                
                                image = ET.SubElement(root, 'image', {
                                    'id': str(image_id),
                                    'name': image_name,
                                    'width': str(width),
                                    'height': str(height)
                                })
                                
                                for _, row in df.iterrows():
                                    if pd.isna(row['class_name']) or pd.isna(row['x1']) or pd.isna(row['y1']) or pd.isna(row['x2']) or pd.isna(row['y2']):
                                        continue
                                    
                                    ET.SubElement(image, 'box', {
                                        'label': str(row['class_name']),
                                        'xtl': str(row['x1']),
                                        'ytl': str(row['y1']),
                                        'xbr': str(row['x2']),
                                        'ybr': str(row['y2']),
                                        'occluded': '0',
                                        'z_order': '0'
                                    })
                                
                                image_id += 1
        
        xml_str = ET.tostring(root, encoding='unicode')
        dom = minidom.parseString(xml_str)
        pretty_xml = dom.toprettyxml(indent='  ')
        
        cvat_directory = os.path.join(self.input_directory, 'cvat')
        os.makedirs(cvat_directory, exist_ok=True)
        xml_output_path = os.path.join(cvat_directory, f'{task_name}.xml')
        
        with open(xml_output_path, 'w', encoding='utf-8') as f:
            f.write(pretty_xml)
        
        return xml_output_path

    def process_page(self, pdf_path, page_num, base_output_directory):
        doc = fitz.open(pdf_path)
        page = doc.load_page(page_num)
        page_df_path = os.path.join(base_output_directory, f'results_yolo/page_{page_num+1}.tsv')
        bareme_df_path = os.path.join(base_output_directory, f'{os.path.basename(pdf_path).replace("_blank.pdf", "")}_page{page_num+1}.tsv')
        tsv_files_produced = 0

        if os.path.exists(page_df_path) and os.path.exists(bareme_df_path):
            page_df = pd.read_csv(page_df_path, delimiter='\t')
            bareme_df = pd.read_csv(bareme_df_path, delimiter='\t')

            page_df = page_df[~page_df['class_name'].str.contains('GraphicZone')]
            
            filter_strings = '(MainZone|MarginText|Title|TableZone)'
            page_df = page_df[page_df['class_name'].str.contains(filter_strings, case=False, regex=True)]

            boxes = page_df[['x1', 'y1', 'x2', 'y2']].values.tolist()
            texts = self.extract_text_from_pdf(pdf_path, page_num, boxes)
            
            page_df['text'] = texts
            page_df.sort_values(by='class_name', ascending=True, inplace=True, key=lambda x: x.str.contains('MainZone'))

            page_df['text_no_spaces'] = page_df['text'].apply(lambda x: ''.join(x.split()))
            page_df.drop_duplicates(subset=['text_no_spaces'], keep='first', inplace=True)
            page_df.drop(columns=['text_no_spaces'], inplace=True)
            
            combined_df = pd.concat([bareme_df, page_df], axis=0, ignore_index=True)
            
            combined_df.sort_values(by='y1', inplace=True)
            
            new_output_directory = os.path.join(base_output_directory, 'final')
            os.makedirs(new_output_directory, exist_ok=True)

            combined_df_output_path = os.path.join(new_output_directory, f'combined_page{page_num+1}.tsv')
            combined_df.to_csv(combined_df_output_path, sep='\t', index=False)
            tsv_files_produced = 1

        doc.close()
        return tsv_files_produced

    def process_all_pages_parallel(self, pdf_path, base_output_directory):
        start_time = time.time()
        doc = fitz.open(pdf_path)
        num_pages = len(doc)
        doc.close()
        results = Parallel(n_jobs=4)(delayed(self.process_page)(pdf_path, page_num, base_output_directory) for page_num in range(num_pages))
        total_tsv_files_produced = sum(results)
        end_time = time.time()
        return end_time - start_time, total_tsv_files_produced

    def process_directory_for_text_extraction(self):
        total_tsv_files = 0
        total_time = 0.0
        files_processed = 0
        last_gc_threshold = 0

        for entry in os.listdir(self.input_directory):
            path = os.path.join(self.input_directory, entry)
            if os.path.isdir(path) and path.endswith('_output'):
                blank_pdf_path = os.path.join(path, f"{os.path.basename(path[:-7])}_blank.pdf")
                if os.path.exists(blank_pdf_path):
                    processing_time, tsv_files_produced = self.process_all_pages_parallel(blank_pdf_path, path)
                    total_tsv_files += tsv_files_produced
                    total_time += processing_time
                    files_processed += 1

                    if files_processed // 10 > last_gc_threshold:
                        gc.collect()
                        print("Garbage Collected!")
                        last_gc_threshold = files_processed // 10

        print(f"Total combined_pageX.tsv files produced: {total_tsv_files}")
        print(f"Total processing time: {total_time:.2f} seconds")
        if total_tsv_files > 0:
            print(f"Average processing time per file: {total_time / total_tsv_files:.2f} seconds")
        else:
            print("No files were produced.")

        task_name = "multi_document_task"
        cvat_xml_path = self.create_cvat_task_xml(task_name)
        print(f"CVAT task XML file created: {cvat_xml_path}")

        return total_tsv_files, total_time, cvat_xml_path