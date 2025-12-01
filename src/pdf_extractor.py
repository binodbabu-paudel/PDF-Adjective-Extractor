"""
PDF Text Extraction Module
"""

import re
import importlib

def import_pdf_library():
    """Import PDF library with fallbacks"""
    libraries = ['pypdf', 'PyPDF2']
    
    for lib_name in libraries:
        try:
            pdf_lib = importlib.import_module(lib_name)
            print(f"✓ Using {lib_name}")
            return pdf_lib
        except ImportError:
            continue
    
    raise ImportError("No PDF library found. Install with: pip install pypdf")

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file
    
    Args:
        pdf_path (str): Path to PDF file
    
    Returns:
        str: Extracted text
    """
    pdf_lib = import_pdf_library()
    
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = pdf_lib.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def clean_text(text):
    """
    Clean extracted text
    
    Args:
        text (str): Raw extracted text
    
    Returns:
        str: Cleaned text
    """
    if not text:
        return ""
    
    # Remove extra whitespaces and newlines
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters
    text = re.sub(r'[^\w\s.,;:!?-]', ' ', text)
    
    return text.strip()
