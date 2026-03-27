"""
Convert Rn2Ywi_rawdata_2026-02-12.txt (JSONL format) to a clean JSON file.
Indented JSON with arrays kept on a single line.
"""

import json

INPUT_FILE = "Rn2Ywi_rawdata_2026-02-12.txt"
OUTPUT_FILE = "Rn2Ywi_rawdata_2026-02-12.json"


def collapse_arrays(json_str):
    """Keep number arrays on one line instead of expanding vertically."""
    lines = json_str.split('\n')
    result = []
    i = 0
    while i < len(lines):
        stripped = lines[i].rstrip()

        # Check if line ends with '[' (start of an array)
        if stripped.endswith('['):
            collected = []
            j = i + 1
            is_number_array = True

            # Collect lines until we find the closing ']'
            while j < len(lines):
                inner = lines[j].strip()

                # Found closing bracket
                if inner == ']' or inner == '],':
                    closing = inner
                    # Build compact array on one line
                    nums = [c.strip().rstrip(',') for c in collected]
                    result.append(f"{stripped}{', '.join(nums)}{closing}")
                    i = j + 1
                    break

                # Check if this element is a number
                val = inner.rstrip(',')
                try:
                    float(val)
                    collected.append(inner)
                    j += 1
                except ValueError:
                    # Not a number array - keep original formatting
                    is_number_array = False
                    break

            if not is_number_array:
                result.append(lines[i])
                i += 1
        else:
            result.append(lines[i])
            i += 1

    return '\n'.join(result)


def convert():
    # Read JSONL (one JSON object per line)
    records = []
    skipped = 0

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                skipped += 1
                print(f"Skipped line {line_num}: {e}")

    # Generate indented JSON, then collapse arrays to one line
    json_str = json.dumps(records, indent=2, ensure_ascii=False)
    json_str = collapse_arrays(json_str)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(json_str)
        f.write("\n")

    print(f"Done! Converted {len(records)} records to {OUTPUT_FILE}")
    if skipped:
        print(f"Skipped {skipped} invalid lines")


if __name__ == "__main__":
    convert()