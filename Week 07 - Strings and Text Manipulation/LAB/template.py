"""
RECORD CHECK - my version
===========================

Name  : Nicole
Lane  : AI / Data Science
Date  : 04/11/2026

Run it: python template.py
"""

# 1. Parse and clean one raw survey record

def parse_line(raw_line):
    """Cleaning and converting one messy survey record into a dictionary."""

    raw_line = raw_line.strip().lower()

    parts = raw_line.split(",")

    record = {"survey": parts[0].strip()}

    for piece in parts[1:]:
        key, value = piece.split("=", 1)

        key = key.strip()
        value = value.strip()

        record[key] = float(value)

    return record


# 2. determining the survey rating status

def status_of(record):
    """Flag survey records with a rating below 3."""

    if record["rating"] < 3:
        return "FLAGGED"
    else:
        return "OK"




# 3. creating 5 messy survey records

raw_records = [
    "  Survey_2026 , rating=4 , age=23  ",
    "SURVEY_2026,rating=2,age=19",
    "  survey_2027, rating = 5, age = 25 ",
    "Survey_2028 , RATING=1 , AGE=30",
    "   SURVEY_2029  , rating=3 , age=21   "
]


# saving records to text file

with open("messy_records.txt", "w") as file:
    for raw_record in raw_records:
        file.write(raw_record + "\n")



raw_records = []

with open("messy_records.txt", "r") as file:
    for line in file:
        raw_records.append(line)


# 4.processing each record and calculate the summary

total_records = 0
flagged_records = 0

for raw_record in raw_records:

    # Parse the messy record
    record = parse_line(raw_record)

    status = status_of(record)

    print(record, status)

    # Update the counters
    total_records += 1

    if status == "FLAGGED":
        flagged_records += 1


print("\nSUMMARY")
print("Total records:", total_records)
print("Flagged records:", flagged_records)


