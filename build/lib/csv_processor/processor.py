import pandas as pd
import re
import os

class CSVProcessor:
    def __init__(self, eslide_final_path, biotracker_path, output_dir):
        self.eslide_final_path = eslide_final_path
        self.biotracker_path = biotracker_path
        self.output_dir = output_dir
        self.eslide_df = None
        self.biotracker_df = None

    def load_data(self):
        if os.path.isfile(self.eslide_final_path):
            self.eslide_df = pd.read_csv(self.eslide_final_path, dtype=str, encoding='latin1')
        else:
            raise FileNotFoundError(f"{self.eslide_final_path} does not exist.")
        
        if os.path.isfile(self.biotracker_path):
            self.biotracker_df = pd.read_csv(self.biotracker_path, dtype=str, encoding='latin1')
        else:
            raise FileNotFoundError(f"{self.biotracker_path} does not exist.")

    def add_biosource_id(self):
        def get_biosource_id(row):
            if (row['Specie'] == 'Human' or pd.isna(row['Specie'])) and row['Scan Status'] == 'Success':
                sample_value = str(row['Sample']) if pd.notna(row['Sample']) else ''
                if 'cell' not in sample_value.lower() and 'tum' not in sample_value.lower():
                    pattern_3 = re.compile(r'^([A-Za-z]{3})(\d{3})$')
                    pattern_4 = re.compile(r'^([A-Za-z]{3})(\d{4})$')
                    pattern_5 = re.compile(r'^([A-Za-z]{3})(\d{5})$')
                    pattern_6 = re.compile(r'^([A-Za-z]{3})(\d{6})$')
                    match_3 = pattern_3.match(sample_value)
                    match_4 = pattern_4.match(sample_value)
                    match_5 = pattern_5.match(sample_value)
                    match_6 = pattern_6.match(sample_value)
                    if match_6:
                        return sample_value
                    elif match_3:
                        return f"{match_3.group(1)}000{match_3.group(2)}"
                    elif match_4:
                        return f"{match_4.group(1)}00{match_4.group(2)}"
                    elif match_5:
                        return f"{match_5.group(1)}0{match_5.group(2)}"
            return None

        insert_position = self.eslide_df.columns.get_loc("Sample") + 1
        self.eslide_df.insert(insert_position, 'Biosource ID', self.eslide_df.apply(get_biosource_id, axis=1))
        
        biosource_output = os.path.join(self.output_dir, "Final-BiosourceID.csv")
        self.eslide_df.to_csv(biosource_output, index=False)
        print(f"Biosource ID added and file saved as {biosource_output}")

    def merge_and_map(self):
        self.biotracker_df['ID'] = self.biotracker_df['ID'].str.split('-').str[0]
        tissue_type_map = self.biotracker_df.set_index('ID')['Tissue Type'].to_dict()
        supplier_diagnosis_map = self.biotracker_df.set_index('ID')['SupplierMicroscopicDiagnos.SL'].to_dict()
        
        self.eslide_df['Tissues Biosource'] = self.eslide_df['Biosource ID'].map(tissue_type_map)
        self.eslide_df['Pathology'] = self.eslide_df['Biosource ID'].map(supplier_diagnosis_map)
        
        merge_output = os.path.join(self.output_dir, "eSlide-Biosource-Merge.csv")
        self.eslide_df.to_csv(merge_output, index=False)
        print(f"Merged file saved as {merge_output}")

    def filter_data(self):
        filtered_df = self.eslide_df.dropna(subset=['Biosource ID'])
        filtered_output = os.path.join(self.output_dir, "Filtered_Final_Merge.csv")
        filtered_df.to_csv(filtered_output, index=False)
        print(f"Filtered file saved as {filtered_output}")

    def process(self):
        self.load_data()
        self.add_biosource_id()
        self.merge_and_map()
        self.filter_data()
