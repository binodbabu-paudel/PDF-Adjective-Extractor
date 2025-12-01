"""
Main script for PDF Adjective Extractor
"""

import os
import sys
from src.pdf_extractor import extract_text_from_pdf, clean_text
from src.text_analyzer import TextAnalyzer

def main():
    """Main execution function"""
    print("=" * 60)
    print("PDF ADJECTIVE EXTRACTOR")
    print("=" * 60)
    
    # Get PDF path
    pdf_path = input("Enter PDF file path (or press Enter for 'data/Nepal.pdf'): ").strip()
    if not pdf_path:
        pdf_path = "data/Nepal.pdf"
    
    # Check if file exists
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' not found.")
        print("Please make sure the PDF file exists.")
        return
    
    # Step 1: Extract text
    print("\n[1/3] Extracting text from PDF...")
    raw_text = extract_text_from_pdf(pdf_path)
    
    if not raw_text:
        print("Failed to extract text from PDF.")
        return
    
    # Step 2: Clean text
    print("[2/3] Cleaning extracted text...")
    cleaned_text = clean_text(raw_text)
    
    # Step 3: Extract adjectives
    print("[3/3] Analyzing text and extracting adjectives...")
    analyzer = TextAnalyzer()
    adjectives = analyzer.extract_adjectives(cleaned_text)
    
    # Step 4: Display results
    if adjectives:
        analysis = analyzer.analyze_adjectives(adjectives)
        
        print("\n" + "=" * 60)
        print("RESULTS SUMMARY")
        print("=" * 60)
        print(f"Total adjectives found: {analysis['total_count']}")
        print(f"Unique adjectives: {analysis['unique_count']}")
        
        print("\nTop 10 most frequent adjectives:")
        print("-" * 40)
        for word, count in analysis['most_common'][:10]:
            print(f"  {word:20} : {count:3}")
        
        # Step 5: Save results
        os.makedirs("output", exist_ok=True)
        output_file = f"output/adjectives_{os.path.basename(pdf_path).split('.')[0]}.txt"
        analyzer.save_results(adjectives, output_file)
        
        print("\n" + "=" * 60)
        print(f"Analysis complete! Check '{output_file}' for detailed results.")
    else:
        print("No adjectives found in the document.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
