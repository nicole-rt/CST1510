"""
RECORD CHECK  -  my version
===========================

Name  : Nicole Tuhwe
Lane  : AI / Data Science
Date  :

Run it:   python template.py
"""


def status_of(percent):
    """Return OVER LIMIT, WARNING or OK for a given percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the amount remaining and the percentage of the limit used."""
    difference = limit - value
    percentage = (value / limit) * 100
    return difference, percentage


def print_report(label, value, limit, difference, percent, status):
    """Print the bordered report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  {'Loaded':<12}: {value:>10.2f}")
    print(f"  {'Expected':<12}: {limit:>10.2f}")
    print(f"  {'Remaining':<12}: {difference:>10.2f}")
    print(f"  {'Percent':<12}: {percent:>10.2f} %")
    print(f"  {'Status':<12}: {status:>10}")
    print("=" * 34)


over_count = 0

while True:
    # INPUT
    label = input("Dataset name (or 'quit' to stop): ")
    if label.lower() == "quit":
        break
    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))

    # PROCESS
    difference, percent = check(value, limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        over_count += 1

    # OUTPUT
    print_report(label, value, limit, difference, percent, status)

print(f"\nRecords over limit: {over_count}")