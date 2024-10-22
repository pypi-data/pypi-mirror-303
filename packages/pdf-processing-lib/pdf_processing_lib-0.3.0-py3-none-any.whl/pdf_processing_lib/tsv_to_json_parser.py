import pandas as pd
import json
import os
import re
from joblib import Parallel, delayed
from time import time
import gc

class TSVtoJSONParser:
    def __init__(self, root_directory):
        self.root_directory = root_directory

    @staticmethod
    def classify_class_name(class_name):
        if pd.isnull(class_name) or class_name == "":
            return "Blank"
        elif "Head" in class_name or "Title" in class_name:
            if class_name not in ["RunningTitleZone", "PageTitleZone-Index"]:
                return "Special"
        return "Regular"

    @staticmethod
    def split_text(text, max_words=350):
        sentences = re.split(r'(?<=[.!?])\s+', text)
        chunks = []
        current_chunk = []
        current_word_count = 0

        for sentence in sentences:
            sentence_word_count = len(sentence.split())
            if current_word_count + sentence_word_count > max_words and current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_word_count = 0
            
            current_chunk.append(sentence)
            current_word_count += sentence_word_count

            # If a single sentence is longer than max_words, split it
            while current_word_count > max_words:
                chunks.append(' '.join(current_chunk[:-1]))
                last_sentence = current_chunk[-1]
                current_chunk = [last_sentence]
                current_word_count = len(last_sentence.split())

        if current_chunk:
            chunks.append(' '.join(current_chunk))

        return chunks

    def parse_tsvs_to_json(self, directory):
        tsv_files = sorted([f for f in os.listdir(directory) if f.endswith('.tsv')],
                           key=lambda x: int(re.search(r'combined_page(\d+).tsv', x).group(1)))
        full_document_name = os.path.basename(os.path.dirname(directory))
        document_name = full_document_name.replace("_output", "")
        json_data = []
        current_section = None
        current_text = ""
        current_pages = []
        
        def create_entry(text, pages):
            return {
                "section": current_section,
                "text": text.strip(),
                "pages": pages,
                "document": document_name,
                "word_count": len(text.split())
            }
        
        for file_name in tsv_files:
            page_number = re.search(r'combined_page(\d+).tsv', file_name).group(1)
            df = pd.read_csv(os.path.join(directory, file_name), sep='\t', encoding='utf-8')
            df['Category'] = df['class_name'].apply(self.classify_class_name)
            df['text'] = df['text'].astype(str)
            for _, row in df.iterrows():
                category = row['Category']
                text = row['text'].strip()
                if category == "Blank":
                    if current_section is not None:
                        for chunk in self.split_text(current_text):
                            json_data.append(create_entry(chunk, current_pages))
                    json_data.append({
                        "section": text,
                        "text": text,
                        "pages": [page_number],
                        "document": document_name,
                        "word_count": len(text.split())
                    })
                    current_section = None
                    current_text = ""
                    current_pages = []
                elif category == "Special":
                    if current_section is not None:
                        for chunk in self.split_text(current_text):
                            json_data.append(create_entry(chunk, current_pages))
                    current_section = text
                    current_text = text
                    current_pages = [page_number]
                else:  # Regular
                    if current_section is None:
                        current_section = text
                        current_text = text
                    else:
                        current_text += " " + text
                    if page_number not in current_pages:
                        current_pages.append(page_number)
                    
                    # Check if we need to split the current text
                    if len(current_text.split()) > 350:
                        chunks = self.split_text(current_text)
                        for chunk in chunks[:-1]:
                            json_data.append(create_entry(chunk, current_pages))
                        current_text = chunks[-1]  # Keep the last chunk for potential continuation
        
        # Finalize the last section if it exists
        if current_section is not None:
            for chunk in self.split_text(current_text):
                json_data.append(create_entry(chunk, current_pages))
        
        json_file_name = f"{document_name}.json"
        json_file_path = os.path.join(directory, json_file_name)
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)
        return json_file_path, len(tsv_files)

    def process_all_final_directories(self):
        final_directories = []
        for subdir, dirs, files in os.walk(self.root_directory):
            if subdir.endswith("final") and "_output" in subdir:
                final_directories.append(subdir)
        
        start_time = time()
        results = Parallel(n_jobs=4)(delayed(self.parse_tsvs_to_json)(directory) for directory in final_directories)
        end_time = time()
        
        total_files_processed = 0
        next_files_treated_milestone = 1000
        next_garbage_collection_milestone = 400
        
        for _, count in results:
            total_files_processed += count
            
            if total_files_processed >= next_files_treated_milestone:
                print(f"{total_files_processed} files were treated")
                next_files_treated_milestone += 1000
            
            if total_files_processed >= next_garbage_collection_milestone:
                gc.collect()
                print("Garbage collection performed")
                next_garbage_collection_milestone += 400
        
        total_time = end_time - start_time
        avg_time_per_file = total_time / total_files_processed if total_files_processed > 0 else 0
        
        print(f"Processed {len(final_directories)} final directories.")
        print(f"Total combined_page files processed: {total_files_processed}")
        print(f"Total processing time: {total_time:.2f} seconds")
        print(f"Average time per file: {avg_time_per_file:.4f} seconds")

        return total_files_processed, total_time, avg_time_per_file