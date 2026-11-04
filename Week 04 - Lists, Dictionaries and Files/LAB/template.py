"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI 
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label, value, limit = line.split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit),
            })
    return records


def check_record(record):
    """Return the percentage used and the status for one record."""
    percent = record["value"] / record["limit"] * 100
    status = "OK" if record["value"] <= record["limit"] else "OVER LIMIT"
    return percent, status


def print_report(label, percent, status):
    """Print one line of the report for a single record."""
    print(f"{label}: {percent:.1f}% used - {status}")


def write_results(path, results):
    """Write one label,status line per result to a file."""
    with open(path, "w") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")


def main():
    """Load the records, report on each, and save the results."""
    try:
        records = load_records("servers.txt")
    except FileNotFoundError:
        print("Could not find servers.txt - starting with no records.")
        records = []

    results = []
    over_count = 0

    for record in records:
        percent, status = check_record(record)
        print_report(record["label"], percent, status)
        results.append((record["label"], status))
        if status == "OVER LIMIT":
            over_count += 1

    print(f"Records over limit: {over_count}")
    write_results("results.txt", results)


main()