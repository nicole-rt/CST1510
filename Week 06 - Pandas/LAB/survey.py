
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    r"C:\Users\User\OneDrive - Middlesex University\CST1510\Week 06 - Pandas\LAB\survey_results.csv"
)

print(df.head())
print(df.dtypes)
print(len(df))

#measuring gap
unanswered = len(df[df["answered"] == 0])
percentage = unanswered / len(df) * 100

print("Unanswered:", unanswered)
print("Unanswered percentage:", percentage)

#filtering
clean_df = df[df["answered"] == 1].copy()

print(clean_df)


category_average = clean_df.groupby("category")["score"].mean()

print(category_average)


category_average = category_average.sort_values(ascending=False)

print(category_average)


clean_df["result"] = clean_df["score"].apply(
    lambda s: "Pass" if s >= 60 else "Fail"
)

print(clean_df[["category", "score", "result"]])


clean_df["result"].value_counts().plot(kind="bar")

plt.title("Survey Pass and Fail Counts")
plt.xlabel("Result")
plt.ylabel("Number of Responses")

plt.savefig("survey_pass_fail.png")
plt.show()


clean_df.to_csv("survey_results_clean.csv", index=False)
