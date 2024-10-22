# PDF Processing Library

This library provides tools for processing PDF documents, images, extracting text, parsing TSV files to JSON, and merging JSON files. It includes functionality for text extraction, image conversion, table detection, object detection using YOLO, CVAT task XML generation, TSV to JSON parsing, and JSON merging with hash generation.

## Installation

```bash
pip install pdf_processing_lib
```

## Usage

```python
from pdf_processing_lib import PDFProcessor, ImageProcessor, TextExtractor, TSVtoJSONParser, JSONMerger

# Process PDFs
pdf_processor = PDFProcessor('path/to/input/directory', 'path/to/output/directory')
pdf_processor.process_directory()

# Process images
image_processor = ImageProcessor('path/to/yolo/model.pt')
image_processor.process_directory('path/to/output/directory')

# Extract text and create CVAT task XML
text_extractor = TextExtractor('path/to/output/directory')
total_files, total_time, cvat_xml_path = text_extractor.process_directory_for_text_extraction()

# Parse TSV files to JSON
tsv_parser = TSVtoJSONParser('path/to/output/directory')
total_files, total_time, avg_time = tsv_parser.process_all_final_directories()

# Merge JSON files and add hash
json_merger = JSONMerger('path/to/json/directory')
output_file, total_entries = json_merger.run('path/to/output/merged.json')
```

## Features

- Extract text and tables from PDFs
- Convert PDF pages to JPG images
- Create versions of PDFs with tables covered
- Process multiple PDFs in parallel
- Perform object detection on images using YOLO
- Process images in batches for efficient memory usage
- Extract text from specific regions in PDFs
- Generate CVAT task XML for annotation purposes
- Parse TSV files to structured JSON format
- Merge multiple JSON files into a single file with added hash keys

## License

This project is licensed under the MIT License - see the LICENSE file for details.
