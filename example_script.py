from csv_processor.processor import CSVProcessor
import os

# Example usage
eslide_final_path = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\YourInputCSV.csv'
biotracker_path = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\YourBiotrackerCSV.csv'
output_dir = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\OutputDirectory'

processor = CSVProcessor(eslide_final_path, biotracker_path, output_dir)
processor.process()

