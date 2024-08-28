CSV Processor Tool
This tool processes CSV files by adding a "Biosource ID" column, merging data with another CSV file, mapping additional columns, and filtering the results. It is designed to automate the process of handling and combining complex datasets with specific ID normalization and mapping requirements.

Features
Add Biosource ID: Automatically generate and add a "Biosource ID" column based on specified patterns in the input data.
Merge and Map Data: Normalize IDs, map data from Biotracker_Extract.csv to eSlide_Final.csv, and add "Tissues Biosource", "Pathology", and "Biosource Pathology" columns.
Filter Data: Filter the data to include only rows with a valid "Biosource ID" and save the results in separate output files.
Installation
Clone the repository and install the package:


git clone https://github.com/yourusername/csv_processor_tool.git
cd csv_processor_tool
pip install .


How to Use the Tool
Step 1: Prepare Your Files
Identify the Files:
You should have two CSV files:

- The primary file you want to process (eSlide_Final.csv).
- The Biotracker file that contains additional data needed for merging (Biotracker_Extract.csv).

Place the Files:
Place both files in a known directory. For example:


C:\Users\U1028428\OneDrive - Sanofi\Bureau\eSlide_Final.csv
C:\Users\U1028428\OneDrive - Sanofi\Bureau\Biotracker_Extract.csv


Step 2: Modify the example_script.py
Edit example_script.py:
Open example_script.py in your text editor. Update the file paths to match the location of your new files:


from csv_processor.processor import CSVProcessor
import os

eslide_final_path = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\eSlide_Final.csv'
biotracker_path = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\Biotracker_Extract.csv'
output_dir = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\OutputDirectory'

processor = CSVProcessor(eslide_final_path, biotracker_path, output_dir)
processor.process()


- Replace eSlide_Final.csv and Biotracker_Extract.csv with the actual names of your files.
- Replace OutputDirectory with the path where you want the processed files to be saved. For example: C:\Users\U1028428\OneDrive - Sanofi\Bureau\ProcessedFiles.


Step 3: Run the Script

1. Run the Script:
   
In the command prompt or terminal, navigate to the directory where example_script.py is located:
cd C:\Users\U1028428\OneDrive - Sanofi\Bureau\csv_processor_tool

Run the script:
python example_script.py


2. Check the Output:
Once the script has run, navigate to the output directory you specified. You should find the processed files there, such as:

Final-BiosourceID.csv
eSlide-Biosource-Merge.csv
Filtered_Final_Merge.csv
Detailed Explanation of the Tool
1. Load Data
The tool loads two CSV files:

eSlide_Final.csv: Contains information related to biosource samples.
Biotracker_Extract.csv: Contains additional data such as tissue type and diagnostic information needed for merging.
2. Add Biosource ID
The tool adds a new column, Biosource ID, to the eSlide_Final.csv data based on the following logic:

If the Specie is Human (or the field is empty) and the Scan Status is Success, the tool checks the Sample column.
If the Sample value does not contain the words "cell" or "tum" and matches specific patterns, a new Biosource ID is generated.
The Biosource ID is formatted for consistency, e.g., converting ABC123 to ABC000123.
3. Merge and Map Data
The tool performs the following operations:

Normalize IDs: Extracts a 3-letter, 6-digit pattern from IDs (e.g., STR001322 from STR001322-001 or EU-AST000212), ignoring prefixes like EU- or suffixes like -001.
Map Tissues Biosource: The Tissues Biosource column is mapped using the Tissue Type from Biotracker_Extract.csv.
Map Pathology: The Pathology column is mapped from SupplierMicroscopicDiagnos.SL. If this value is missing, it falls back to Pri.Sup.CaseDiagnosis-DL.
Add Biosource Pathology: A new column Biosource Pathology is added right after Pathology, containing the value from Pri.Sup.CaseDiagnosis-DL.
4. Filter Data
The tool filters the data to include only rows where the Biosource ID is not empty. This filtered data is saved as a separate file.

Final Output Files
Final-BiosourceID.csv: Contains the eSlide_Final.csv data with the added Biosource ID column.
eSlide-Biosource-Merge.csv: The final merged file containing the mapped Tissues Biosource, Pathology, and Biosource Pathology columns.
Filtered_Final_Merge.csv: A filtered version of the merged file, containing only rows with a valid Biosource ID.
This tool automates complex data processing tasks, ensuring accuracy and consistency in the final output files.

