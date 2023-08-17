# Task 5 - Create a column category and store it in RESULTS.xlsx file

import pandas as pd

file1 = pd.read_excel("RESULT1.xlsx")
file2 = pd.read_excel("RESULT2.xlsx")

all_data = pd.concat([file1, file2], ignore_index=True)

all_data["CATEGORY"] = None
category = " "

for i in range(len(all_data["PERCENTAGE"])):
    if all_data["PERCENTAGE"][i] >= 80:
        category = "SCHOLAR"
    elif 50 <= all_data["PERCENTAGE"][i] <= 79:
        category = "AVERAGE"
    elif all_data["PERCENTAGE"][i] <= 50:
        category = "WEAK"

    all_data["CATEGORY"][i] = category

all_data.to_excel("RESULTS.xlsx", index=False)

print(all_data)
