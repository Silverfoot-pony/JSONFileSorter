import os
import json
import glob
import argparse


def merge_json(folder, filename, output_file):
    json_files = glob.glob(os.path.join(folder, "**", filename), recursive=True)

    if not json_files:
        print(f"No files named '{filename}' found under: {folder}")
        return

    print(f"Found {len(json_files)} file(s) to merge.")
    merged_data = []
    errors = 0

    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    merged_data.extend(data)
                else:
                    merged_data.append(data)
            except json.JSONDecodeError as e:
                print(f"Skipping {file}: {e}")
                errors += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, indent=4, ensure_ascii=False)

    print(f"Merged {len(merged_data)} records from {len(json_files) - errors} file(s) -> {output_file}")
    if errors:
        print(f"{errors} file(s) skipped due to errors.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recursively merge JSON files from a folder tree.")
    parser.add_argument("folder", help="Root folder to search for JSON files")
    parser.add_argument("--filename", default="messages.json", metavar="FILENAME",
                        help="Filename pattern to match (default: messages.json)")
    parser.add_argument("--output", help="Output file path (default: <folder>/merged_<filename>)")
    args = parser.parse_args()

    if not args.output:
        args.output = os.path.join(args.folder, f"merged_{args.filename}")

    merge_json(args.folder, args.filename, args.output)
