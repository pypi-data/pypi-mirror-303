from setuptools import setup, find_packages

setup(
    name="pdf_processing_lib",
    version="0.3.0",  
    packages=find_packages(),
    install_requires=[
        'PyMuPDF',
        'pdfplumber',
        'joblib',
        'tqdm',
        'ultralytics',
        'supervision',
        'opencv-python',
        'pandas',
        'Pillow',
    ],
    author="Carlos Rosas",
    author_email="crosashinostroza@gmail.com",
    description="A library for processing PDF documents, images, extracting text, parsing TSV to JSON, and merging JSON files",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pdf_processing_lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)