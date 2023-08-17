# Task 3 - Print all data with total greater than 200

import pandas as pd

file1 = pd.read_excel("RESULT1.xlsx")
file2 = pd.read_excel("RESULT2.xlsx")

all_data = pd.concat([file1, file2], ignore_index=True)

index = 0
sorted1 = all_data.sort_values(["TOTAL"], ascending=False, ignore_index=True)

for i in range(len(sorted1["TOTAL"])):
    if sorted1["TOTAL"][i] >= 200:
        index = i

print(sorted1.head(index + 1))

# index = []

# for i in range(len(all_data["TOTAL"])):
#     if all_data["TOTAL"][i] > 200:
#         index.append(i)

# print(all_data.iloc[index])
