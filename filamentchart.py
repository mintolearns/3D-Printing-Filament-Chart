import pandas as pd
import json

# Load the clean JSON structure back into Python
with open("filaments.json", "r") as f:
    clean_json_data = json.load(f)

# Convert JSON data to a DataFrame
clean_df = pd.DataFrame.from_dict(clean_json_data, orient='index')
clean_df.index.name = "Filament Type"
clean_df.reset_index(inplace=True)

# Save as Excel file
excel_file_path = "output.xlsx"
clean_df.to_excel(excel_file_path, index=False)
