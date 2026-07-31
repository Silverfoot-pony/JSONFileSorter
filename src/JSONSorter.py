import json
import argparse
from pathlib import Path


def sort_json(input_file, sort_by, output_file, reverse=False):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of objects.")

    if data and sort_by not in data[0]:
        raise KeyError(f"Column '{sort_by}' not found in data.")

    sorted_data = sorted(data, key=lambda x: x[sort_by], reverse=reverse)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, indent=4, ensure_ascii=False)

    print(f"Sorted {len(sorted_data)} records by '{sort_by}' -> {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort a JSON file by a specified column.")
    parser.add_argument("input", help="Path to the input JSON file")
    parser.add_argument("--sort-by", required=True, metavar="COLUMN", help="Column name to sort by")
    parser.add_argument("--output", help="Output file path (default: <input>_sorted.json)")
    parser.add_argument("--reverse", action="store_true", help="Sort in descending order")
    args = parser.parse_args()

    if not args.output:
        p = Path(args.input)
        args.output = str(p.with_stem(p.stem + "_sorted"))

    sort_json(args.input, args.sort_by, args.output, args.reverse)
