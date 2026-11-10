
"""
RECORD CHECK - my version
===========================

Name  : Nicole Tuhwe
Lane  : AI / Data Science
Date  : 26/10/2026
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("records.csv")

#Calculate percentage
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100

# Add status column using a lambda
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)



print(df)


print("\nRecords requiring attention:")
print(df[df["status"] != "OK"])

# Group by status and count records
print("\nStatus counts:")
print(df.groupby("status").size())


df.to_csv("records_report.csv", index=False)


df["status"].value_counts().plot(kind="bar")

plt.title("AI Dataset Status Counts")
plt.xlabel("Status")
plt.ylabel("Number of Datasets")


plt.savefig("status_counts.png")
plt.show()
