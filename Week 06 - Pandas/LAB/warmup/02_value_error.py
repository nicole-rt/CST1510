# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],  # 3 labels
    "value": [87, 120, 95],               #Added a third value
})

print(df)