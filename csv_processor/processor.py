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
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        self.eslide_df.to_csv(biosource_output, index=False)
        print(f"Biosource ID added and file saved as {biosource_output}")

    def merge_and_map(self):
        # Normalize the ID column to extract the 3-letter, 6-digit pattern
        def normalize_id(id_value):
            if isinstance(id_value, str):  # Ensure the ID is a string
                match = re.search(r'[A-Za-z]{3}\d{6}', id_value)
                return match.group(0) if match else None
            return None  # Return None if the value is not a string
        
        # Create mappings based on the normalized ID
        self.biotracker_df['Base ID'] = self.biotracker_df['ID'].apply(normalize_id)
        tissue_type_map = self.biotracker_df.groupby('Base ID')['Tissue Type'].first().to_dict()
        supplier_diagnosis_map = self.biotracker_df.groupby('Base ID')['SupplierMicroscopicDiagnos.SL'].first().to_dict()
        pri_sup_case_diag_map = self.biotracker_df.groupby('Base ID')['Pri.Sup.CaseDiagnosis-DL'].first().to_dict()

        # Map the Tissues Biosource column from the Tissue Type
        self.eslide_df['Tissues Biosource'] = self.eslide_df['Biosource ID'].apply(lambda id_val: tissue_type_map.get(normalize_id(id_val), None))
        
        # Use the normalized ID internally for mapping Pathology
        def map_pathology(row):
            normalized_id = normalize_id(row['Biosource ID'])
            supplier_diag = supplier_diagnosis_map.get(normalized_id, None)
            pri_sup_diag = pri_sup_case_diag_map.get(normalized_id, None)
            
            if pd.notna(supplier_diag) and supplier_diag.strip():
                return supplier_diag
            elif pd.notna(pri_sup_diag) and pri_sup_diag.strip():
                return pri_sup_diag
            else:
                return None
        
        self.eslide_df['Pathology'] = self.eslide_df.apply(map_pathology, axis=1)
        
        # Insert the "Biosource Pathology" column right after the "Pathology" column
        pathology_position = self.eslide_df.columns.get_loc("Pathology") + 1
        self.eslide_df.insert(pathology_position, 'Biosource Pathology', self.eslide_df.apply(
            lambda row: pri_sup_case_diag_map.get(normalize_id(row['Biosource ID']), None), axis=1))
        
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
