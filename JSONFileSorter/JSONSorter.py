import json

def sort_json_by_id(input_file, output_file):
    # Load JSON data from file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Sort the list of messages by the 'ID' field
    sorted_data = sorted(data, key=lambda x: x['[column]']) #specify here the column to filter by

    # Write the sorted data back to another JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    input_path = "merged_filename.json"
    output_path = "sorted_filename.json"
    sort_json_by_id(input_path, output_path)
    print(f"Sorted data written to {output_path}")
