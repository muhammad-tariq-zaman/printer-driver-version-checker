"""Check printer drivers against minimum versions per model.

Usage: python3 main.py printers.csv
CSV columns: printer,model,driver_version
Minimum versions are built in per model; unknown models are reported
as UNKNOWN rather than guessed. Rows get OK, OUTDATED or UNKNOWN.
"""
import argparse, csv, sys

MINIMUM = {"HP-LaserJet-M404": (2, 1), "Canon-iR-ADV": (3, 0),
           "Brother-HL-L8360": (1, 5), "Epson-WF-C5790": (4, 2)}


def parse_version(text):
    parts = text.strip().split(".")
    if len(parts) < 2 or not all(p.isdigit() for p in parts[:2]):
        return None
    return (int(parts[0]), int(parts[1]))


def check(model, version):
    if model not in MINIMUM:
        return "UNKNOWN", "no minimum on record for this model"
    parsed = parse_version(version)
    if parsed is None:
        return "UNKNOWN", "unparsable driver version"
    if parsed < MINIMUM[model]:
        return "OUTDATED", "below minimum " + ".".join(map(str, MINIMUM[model]))
    return "OK", "meets minimum"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    outdated = 0
    with open(args.path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            verdict, reason = check(row["model"].strip(), row["driver_version"].strip())
            if verdict == "OUTDATED":
                outdated += 1
            print(f"{row['printer']}: {verdict} ({reason})")
    print(f"{outdated} printer(s) with outdated drivers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
