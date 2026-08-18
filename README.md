# JSONFileSorter
Small repository with python files that let a user merge, sort and filter large and large amounts of JSON files at once.
I used these files to work my way through a large amount of files after requesting my Discord Data Package. Seemed to work alright ig.

## Usage

Each script is a standalone CLI tool (uses only the Python standard library).

### JSONMerger.py

Recursively finds all files matching a filename under a folder tree and merges them into one JSON file.

```
python src/JSONMerger.py <folder> [--filename FILENAME] [--output OUTPUT]
```

- `folder` — root folder to search for JSON files
- `--filename` — filename to match (default: `messages.json`)
- `--output` — output file path (default: `<folder>/merged_<filename>`)

Example:
```
python src/JSONMerger.py ./discord-package --filename messages.json --output merged.json
```

### JSONSorter.py

Sorts a JSON file (a list of objects) by a given field.

```
python src/JSONSorter.py <input> --sort-by COLUMN [--output OUTPUT] [--reverse]
```

- `input` — path to the input JSON file
- `--sort-by` — field name to sort by (required)
- `--output` — output file path (default: `<input>_sorted.json`)
- `--reverse` — sort in descending order

Example:
```
python src/JSONSorter.py merged.json --sort-by Timestamp --output sorted.json
```

### JSONFilter.py

Filters a JSON file (a list of objects) down to only the specified fields.

```
python src/JSONFilter.py <input> --columns COLUMN [COLUMN ...] [--output OUTPUT]
```

- `input` — path to the input JSON file
- `--columns` — one or more field names to keep (required)
- `--output` — output file path (default: `<input>_filtered.json`)

Example:
```
python src/JSONFilter.py sorted.json --columns Timestamp Contents --output filtered.json
```
