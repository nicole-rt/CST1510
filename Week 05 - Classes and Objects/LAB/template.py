
"""
RECORD CHECK - my version
===========================

Name  :
Lane  : AI / Data Science
Date  : 16/10/2026

Run it: python template.py
"""

class Record:

    def __init__(self, label, value, limit):
        """Store the dataset name, rows loaded and rows expected."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the percentage of rows loaded."""
        percentage = (self.value / self.limit) * 100

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"



def load_records(path):
    """Read a file and return a list of Record objects."""

    records = []

    with open(path, "r") as file:

        for line in file:
            label, value, limit = line.strip().split(",")

            # Convert numerical values into floats
            record = Record(label, float(value), float(limit))

            # Add the record object to the list
            records.append(record)

    return records



records = load_records(r"C:\Users\User\OneDrive - Middlesex University\CST1510\Week 05 - Classes and Objects\LAB\records.txt")

#report for each record
over_limit_count = 0

for record in records:

    result = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    #record details
    print(f"  Rows loaded   : {record.value}")
    print(f"  Rows expected : {record.limit}")
    print(f"  Status        : {result}")

    if result == "OVER LIMIT":
        over_limit_count += 1

    print("=" * 34)


print()
print(f"Total records: {len(records)}")
print(f"Records OVER LIMIT: {over_limit_count}")
