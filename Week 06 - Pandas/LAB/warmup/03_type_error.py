# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({
    "value": ["87", "120", "45"],
    "limit": [100, 100, 100]
})

#Converted the value column from strings to integers
df["value"] = df["value"].astype(int)

# Calculate percentage
df["percent"] = (df["value"] / df["limit"]) * 100

print(df)