"""
Text Analysis Module for Adjective Extraction
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import Counter

class TextAnalyzer:
    def __init__(self):
        """Initialize NLTK resources"""
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('taggers/averaged_perceptron_tagger')
        except LookupError:
            print("Downloading NLTK data...")
            nltk.download('punkt', quiet=True)
            nltk.download('averaged_perceptron_tagger', quiet=True)
    
    def extract_adjectives(self, text):
        """
        Extract adjectives from text
        
        Args:
            text (str): Input text
        
        Returns:
            list: List of adjectives
        """
        if not text:
            return []
        
        # Tokenize and tag
        tokens = word_tokenize(text)
        tagged_words = pos_tag(tokens)
        
        # Extract adjectives (JJ, JJR, JJS tags)
        adjectives = [
            word.lower() for word, tag in tagged_words 
            if tag in ['JJ', 'JJR', 'JJS']
        ]
        
        return adjectives
    
    def analyze_adjectives(self, adjectives):
        """
        Analyze extracted adjectives
        
        Args:
            adjectives (list): List of adjectives
        
        Returns:
            dict: Analysis results
        """
        if not adjectives:
            return {}
        
        adj_counter = Counter(adjectives)
        
        return {
            'total_count': len(adjectives),
            'unique_count': len(set(adjectives)),
            'most_common': adj_counter.most_common(20),
            'all_adjectives': adjectives,
            'unique_adjectives': sorted(set(adjectives))
        }
    
    def save_results(self, adjectives, output_path="output/adjectives_list.txt"):
        """
        Save analysis results to file
        
        Args:
            adjectives (list): List of adjectives
            output_path (str): Output file path
        """
        analysis = self.analyze_adjectives(adjectives)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("ADJECTIVES EXTRACTION RESULTS\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"Total adjectives found: {analysis['total_count']}\n")
            f.write(f"Unique adjectives: {analysis['unique_count']}\n\n")
            
            f.write("Top 20 Most Frequent Adjectives:\n")
            f.write("-" * 40 + "\n")
            for word, count in analysis['most_common']:
                f.write(f"{word:20} : {count:3} times\n")
            
            f.write("\n" + "=" * 60 + "\n")
            f.write("ALL ADJECTIVES (in order of appearance):\n")
            f.write("=" * 60 + "\n")
            for i, adj in enumerate(analysis['all_adjectives'], 1):
                if i % 5 == 0:
                    f.write(f"{adj}\n")
                else:
                    f.write(f"{adj:20}")
            
            f.write("\n\n" + "=" * 60 + "\n")
            f.write("UNIQUE ADJECTIVES (alphabetical order):\n")
            f.write("=" * 60 + "\n")
            for i, adj in enumerate(analysis['unique_adjectives'], 1):
                if i % 5 == 0:
                    f.write(f"{adj}\n")
                else:
                    f.write(f"{adj:20}")
        
        print(f"✓ Results saved to {output_path}")
