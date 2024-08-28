from csv_processor.processor import CSVProcessor
import os

# Example usage
eslide_final_path = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\Final-Files/Final-Extract.csv'
biotracker_path = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\Biotracker_Extract.csv'
output_dir = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau/test-monday'

processor = CSVProcessor(eslide_final_path, biotracker_path, output_dir)
processor.process()
