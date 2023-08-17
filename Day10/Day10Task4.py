# Task 4 - Store all data with TOTAL less than 100 in weakstudents.xlsx file

import pandas as pd

file1 = pd.read_excel("RESULT1.xlsx")
file2 = pd.read_excel("RESULT2.xlsx")

all_data = pd.concat([file1, file2], ignore_index=True)

index1 = 0
sorted2 = all_data.sort_values(["TOTAL"], ascending=True, ignore_index=True)

for i in range(len(sorted2["TOTAL"])):
    if sorted2["TOTAL"][i] <= 100:
        index1 = i

weak_students = sorted2.head(index1 + 1)


# index = []

# for i in range(len(all_data["TOTAL"])):
#     if all_data["TOTAL"][i] <= 100:
#         index.append(i)

# weak_students = all_data.iloc[index]

# print(weak_students)
weak_students.to_excel("weakstudents.xlsx", index=False)
