import json
import argparse
from pathlib import Path


def filter_json(input_file, columns, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of objects.")

    if data:
        missing = [c for c in columns if c not in data[0]]
        if missing:
            raise KeyError(f"Column(s) not found in data: {', '.join(missing)}")

    filtered = [{col: record[col] for col in columns if col in record} for record in data]

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered, f, indent=4, ensure_ascii=False)

    print(f"Filtered {len(filtered)} records -> {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter a JSON file to keep only specified columns.")
    parser.add_argument("input", help="Path to the input JSON file")
    parser.add_argument("--columns", nargs="+", required=True, metavar="COLUMN", help="Column name(s) to keep")
    parser.add_argument("--output", help="Output file path (default: <input>_filtered.json)")
    args = parser.parse_args()

    if not args.output:
        p = Path(args.input)
        args.output = str(p.with_stem(p.stem + "_filtered"))

    filter_json(args.input, args.columns, args.output)
