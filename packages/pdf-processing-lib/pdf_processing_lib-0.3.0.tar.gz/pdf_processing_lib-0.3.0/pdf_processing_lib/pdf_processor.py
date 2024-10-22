import pdfplumber
import fitz  # PyMuPDF
import csv
import os
import time
import traceback
import gc
from joblib import Parallel, delayed
from tqdm import tqdm

class PDFProcessor:
    def __init__(self, input_path, output_directory):
        self.input_path = input_path
        self.output_directory = output_directory

    @staticmethod
    def clean_cell(cell):
        if cell is None:
            return ''
        return cell.replace('\n', ' ')

    def pdf_to_jpg_original(self, pdf_path, output_images):
        os.makedirs(output_images, exist_ok=True)
        doc = fitz.open(pdf_path)
        jpg_count = 0
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            output_path = os.path.join(output_images, f"{base_name}_page{page_num + 1}.jpg")
            pix.save(output_path)
            jpg_count += 1
        doc.close()
        return jpg_count

    def extract_text_tables_and_save(self, pdf_path, output_directory):
        os.makedirs(output_directory, exist_ok=True)
        global_table_counter = 1
        pdf_basename = os.path.splitext(os.path.basename(pdf_path))[0]

        with pdfplumber.open(pdf_path) as pdf, fitz.open(pdf_path) as doc:
            tables = []
            for page_num, plumb_page in enumerate(pdf.pages):
                # Save coordinates of text and tables
                coord_tsv_filename = os.path.join(output_directory, f"{pdf_basename}_page{page_num + 1}.tsv")
                with open(coord_tsv_filename, 'w', newline='', encoding='utf-8') as coord_file:
                    writer = csv.writer(coord_file, delimiter='\t')
                    writer.writerow(['text', 'x1', 'y1', 'x2', 'y2'])
                    tables = plumb_page.find_tables()
                    if tables:
                        for i, table in enumerate(tables):
                            x1, y1, x2, y2 = table.bbox
                            writer.writerow([f"table_{global_table_counter + i}", x1, y1, x2, y2])
                
                # Save table contents
                for i, table in enumerate(tables):
                    tsv_content = [self.clean_cell(cell) for row in table.extract() for cell in row]
                    table_tsv_filename = os.path.join(output_directory, f"{pdf_basename}_page{page_num+1}_table{global_table_counter}.tsv")
                    with open(table_tsv_filename, 'w', newline='', encoding='utf-8') as tsv_file:
                        writer = csv.writer(tsv_file, delimiter='\t')
                        writer.writerows([[cell] for cell in tsv_content])

                    global_table_counter += 1

    def cover_tables_in_pdf(self, pdf_path, output_path):
        table_areas = []
        with pdfplumber.open(pdf_path) as pdf:
            for page_number, page in enumerate(pdf.pages):
                for table in page.find_tables():
                    table_areas.append((page_number, table.bbox))
        doc = fitz.open(pdf_path)
        for page_number, bbox in table_areas:
            page = doc[page_number]
            rect = fitz.Rect(bbox[0], bbox[1], bbox[2], bbox[3])
            shape = page.new_shape()
            shape.draw_rect(rect)
            shape.finish(width=1, color=(1, 1, 1), fill=(1, 1, 1))
            shape.commit()
        doc.save(output_path, garbage=4, deflate=True)
        doc.close()

    def pdf_to_jpg(self, blank_path, output_images):
        os.makedirs(output_images, exist_ok=True)
        doc = fitz.open(blank_path)
        jpg_count = 0
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            output_path = os.path.join(output_images, f"page_{page_num + 1}.jpg")
            pix.save(output_path)
            jpg_count += 1
        doc.close()
        return jpg_count

    def process_single_pdf(self, pdf_path):
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_directory = os.path.join(self.output_directory, base_name + "_output")
        
        try:
            self.extract_text_tables_and_save(pdf_path, output_directory)
            
            # Create original images
            output_images_original = os.path.join(output_directory, base_name + "_images_original")
            jpg_count_original = self.pdf_to_jpg_original(pdf_path, output_images_original)
            
            # Create blank images (with tables covered)
            output_path = os.path.join(output_directory, base_name + "_blank.pdf")
            self.cover_tables_in_pdf(pdf_path, output_path)
            output_images = os.path.join(output_directory, base_name + "_images")
            jpg_count = self.pdf_to_jpg(output_path, output_images)
            
            return jpg_count + jpg_count_original  # Return total number of JPGs created
        except Exception as e:
            with open("processing_errors.log", "a") as log_file:
                log_file.write(f"Error processing {pdf_path}: {str(e)}\n")
                traceback.print_exc(file=log_file)
            return 0

    def process_directory(self):
        start_time = time.time()
        
        pdf_paths = [os.path.join(self.input_path, f) for f in os.listdir(self.input_path) if f.endswith('.pdf')]
        total_jpg_count = 0
        
        chunk_size = 25

        for start_idx in range(0, len(pdf_paths), chunk_size):
            end_idx = start_idx + chunk_size
            pdf_chunk = pdf_paths[start_idx:end_idx]
            
            chunk_jpg_count = sum(Parallel(n_jobs=4)(delayed(self.process_single_pdf)(pdf_path) for pdf_path in tqdm(pdf_chunk, desc="Processing PDFs")))
            total_jpg_count += chunk_jpg_count

            gc.collect()
        
        end_time = time.time()
        total_time = end_time - start_time
        avg_time_per_page = total_time / total_jpg_count if total_jpg_count else 0
        
        print(f"Total pages processed: {total_jpg_count}")
        print(f"Total processing time: {total_time:.2f} seconds")
        print(f"Average time per page: {avg_time_per_page:.2f} seconds/page")