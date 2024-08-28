Outil de Traitement de Fichiers CSV

Cet outil traite les fichiers CSV en ajoutant une colonne "Biosource ID", en fusionnant les données avec un autre fichier CSV, en mappant des colonnes supplémentaires et en filtrant les résultats. Il est conçu pour automatiser le processus de gestion et de combinaison de jeux de données complexes avec des exigences spécifiques de normalisation des identifiants et de mappage.

Fonctionnalités
- Ajouter un Biosource ID : Génère automatiquement et ajoute une colonne "Biosource ID" en fonction de motifs spécifiés dans les données d'entrée.
- Fusionner et Mapper les Données : Normalise les identifiants, mappe les données de Biotracker_Extract.csv vers eSlide_Final.csv, et ajoute les colonnes "Tissues Biosource", "Pathology" et "Biosource Pathology".
- Filtrer les Données : Filtre les données pour n'inclure que les lignes avec un "Biosource ID" valide et enregistre les résultats dans des fichiers de sortie séparés.
  
Installation
Clonez le dépôt et installez le package :

'git clone https://github.com/votrenomutilisateur/csv_processor_tool.git
cd csv_processor_tool
pip install .'

Comment Utiliser l'Outil

Étape 1 : Préparez Vos Fichiers
Identifiez les Fichiers :
Vous devez avoir deux fichiers CSV :

- Le fichier principal que vous souhaitez traiter (eSlide_Final.csv).
- Le fichier Biotracker qui contient des données supplémentaires nécessaires pour la fusion (Biotracker_Extract.csv).
  
Placez les Fichiers :
Placez les deux fichiers dans un répertoire connu. Par exemple :

C:\Users\U1028428\OneDrive - Sanofi\Bureau\eSlide_Final.csv
C:\Users\U1028428\OneDrive - Sanofi\Bureau\Biotracker_Extract.csv


Étape 2 : Modifiez le example_script.py
Modifiez example_script.py :
Ouvrez example_script.py dans votre éditeur de texte. Mettez à jour les chemins des fichiers pour qu'ils correspondent à l'emplacement de vos nouveaux fichiers :

from csv_processor.processor import CSVProcessor
import os

eslide_final_path = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\eSlide_Final.csv'
biotracker_path = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\Biotracker_Extract.csv'
output_dir = r'C:\Users\U1028428\OneDrive - Sanofi\Bureau\OutputDirectory'

processor = CSVProcessor(eslide_final_path, biotracker_path, output_dir)
processor.process()


- Remplacez eSlide_Final.csv et Biotracker_Extract.csv par les noms réels de vos fichiers.
- Remplacez OutputDirectory par le chemin où vous souhaitez enregistrer les fichiers traités. Par exemple : C:\Users\U1028428\OneDrive - Sanofi\Bureau\ProcessedFiles.


Étape 3 : Exécutez le Script

1. Exécutez le Script :

Dans l'invite de commande ou le terminal, accédez au répertoire où se trouve example_script.py :

cd C:\Users\U1028428\OneDrive - Sanofi\Bureau\csv_processor_tool

Exécutez le script :
python example_script.py


2. Vérifiez la Sortie :
Une fois le script exécuté, accédez au répertoire de sortie que vous avez spécifié. Vous devriez y trouver les fichiers traités, tels que :

- Final-BiosourceID.csv
- eSlide-Biosource-Merge.csv
- Filtered_Final_Merge.csv
- 
Explication Détaillée de l'Outil
1. Chargement des Données
   
L'outil charge deux fichiers CSV :

- eSlide_Final.csv : Contient des informations relatives aux échantillons de biosource.
- Biotracker_Extract.csv : Contient des données supplémentaires telles que le type de tissu et les informations de diagnostic nécessaires pour la fusion.

2. Ajout du Biosource ID
L'outil ajoute une nouvelle colonne, Biosource ID, aux données de eSlide_Final.csv selon la logique suivante :

- Si l'espèce est "Human" (ou si le champ est vide) et que le statut de numérisation est "Success", l'outil vérifie la colonne Sample.
- Si la valeur de l'échantillon ne contient pas les mots "cell" ou "tum" et correspond à des motifs spécifiques, un nouveau Biosource ID est généré.
- Le Biosource ID est formaté pour assurer la cohérence, par exemple en convertissant ABC123 en ABC000123.


3. Fusion et Mapping des Données
L'outil effectue les opérations suivantes :

- Normalisation des Identifiants : Extrait un motif de 3 lettres et 6 chiffres des identifiants (par exemple, STR001322 à partir de STR001322-001 ou EU-AST000212), en ignorant les préfixes comme EU- ou les suffixes comme -001.
- Mapping du Tissues Biosource : La colonne Tissues Biosource est mappée en utilisant le Tissue Type du fichier Biotracker_Extract.csv.
- Mapping du Pathology : La colonne Pathology est mappée à partir de SupplierMicroscopicDiagnos.SL. Si cette valeur est manquante, elle est remplacée par Pri.Sup.CaseDiagnosis-DL.
- Ajout du Biosource Pathology : Une nouvelle colonne Biosource Pathology est ajoutée juste après Pathology, contenant la valeur de Pri.Sup.CaseDiagnosis-DL.



4. Filtrage des Données
L'outil filtre les données pour n'inclure que les lignes où le Biosource ID n'est pas vide. Ces données filtrées sont enregistrées dans un fichier séparé.

Fichiers de Sortie Finales
- Final-BiosourceID.csv : Contient les données de eSlide_Final.csv avec la colonne Biosource ID ajoutée.
- eSlide-Biosource-Merge.csv : Le fichier fusionné final contenant les colonnes Tissues Biosource, Pathology et Biosource Pathology mappées.
- Filtered_Final_Merge.csv : Une version filtrée du fichier fusionné, contenant uniquement les lignes avec un Biosource ID valide.


Cet outil automatise les tâches de traitement de données complexes, garantissant précision et cohérence dans les fichiers de sortie finaux.



-English- 


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

- If the Specie is Human (or the field is empty) and the Scan Status is Success, the tool checks the Sample column.
- If the Sample value does not contain the words "cell" or "tum" and matches specific patterns, a new Biosource ID is generated.
- The Biosource ID is formatted for consistency, e.g., converting ABC123 to ABC000123.

  
3. Merge and Map Data
The tool performs the following operations:

- Normalize IDs: Extracts a 3-letter, 6-digit pattern from IDs (e.g., STR001322 from STR001322-001 or EU-AST000212), ignoring prefixes like EU- or suffixes like -001.
- Map Tissues Biosource: The Tissues Biosource column is mapped using the Tissue Type from Biotracker_Extract.csv.
- Map Pathology: The Pathology column is mapped from SupplierMicroscopicDiagnos.SL. If this value is missing, it falls back to Pri.Sup.CaseDiagnosis-DL.
- Add Biosource Pathology: A new column Biosource Pathology is added right after Pathology, containing the value from Pri.Sup.CaseDiagnosis-DL.

  
4. Filter Data
The tool filters the data to include only rows where the Biosource ID is not empty. This filtered data is saved as a separate file.

Final Output Files

- Final-BiosourceID.csv: Contains the eSlide_Final.csv data with the added Biosource ID column.
- eSlide-Biosource-Merge.csv: The final merged file containing the mapped Tissues Biosource, Pathology, and Biosource Pathology columns.
- Filtered_Final_Merge.csv: A filtered version of the merged file, containing only rows with a valid Biosource ID.

  
This tool automates complex data processing tasks, ensuring accuracy and consistency in the final output files.

