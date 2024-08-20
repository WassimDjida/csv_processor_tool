# CSV Processor Tool

This tool processes CSV files by adding a "Biosource ID" column, merging data with another CSV file, and filtering the results.

## Installation

Clone the repository and install the package:

```bash
git clone https://github.com/yourusername/csv_processor_tool.git
cd csv_processor_tool
pip install .

### How to use the Tool

Step 1: Prepare Your Files
Identify the Files:

You should have two CSV files:
 - The primary file you want to process (let’s call it YourInputCSV.csv).
 - The Biotracker file that contains additional data needed for merging (let’s call it YourBiotrackerCSV.csv).
 
Place the Files:

Place both files in a known directory. For example:
C:\Users\U1028428\OneDrive - Sanofi\Bureau\YourInputCSV.csv
C:\Users\U1028428\OneDrive - Sanofi\Bureau\YourBiotrackerCSV.csv


Step 2: Modify the example_script.py

- Edit example_script.py:

Open example_script.py in your text editor.
Update the file paths to match the location of your new files:

        from csv_processor.processor import CSVProcessor
        import os

        # Example usage
        eslide_final_path = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\YourInputCSV.csv'
        biotracker_path = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\YourBiotrackerCSV.csv'
        output_dir = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\OutputDirectory'

        processor = CSVProcessor(eslide_final_path, biotracker_path, output_dir)
        processor.process()

-  Replace YourInputCSV.csv and YourBiotrackerCSV.csv with the actual names of your files.
-  Replace OutputDirectory with the path where you want the processed files to be saved. For example: C:\Users\U1028428\OneDrive - Sanofi\Bureau\ProcessedFiles.

Step 3: Run the Script

- 1 Run the Script:

In the command prompt or terminal, navigate to the directory where example_script.py is located:

        cd C:\Users\U1028428\OneDrive - Sanofi\Bureau\csv_processor_tool

Run the script:

        python example_script.py

- 2 Check the Output:

Once the script has run, navigate to the output directory you specified.
You should find the processed files there, such as:
Final-BiosourceID.csv
eSlide-Biosource-Merge.csv
Filtered_Final_Merge.csv


