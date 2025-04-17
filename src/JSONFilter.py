import pandas as pd
import json

# Load the JSON data from a file
with open(r'address_to_file.json', 'r', encoding="utf-8") as f: #place here the address to the JSON file to be filtered.
    data = json.load(f)

# Convert the loaded data to a pandas DataFrame
df = pd.DataFrame(data)

# Select only the '[column]' column
df_contents = df[['[column]']]

# Convert the DataFrame to a list of dictionaries (for JSON output)
output_data = df_contents.to_dict(orient='records')

# Save the result to a new JSON file with proper commas
with open('JSONFiltered.json', 'w') as f: #specify the file name of the processed data.
    json.dump(output_data, f, indent=4)

# Print the filtered contents (optional)
print(output_data)
