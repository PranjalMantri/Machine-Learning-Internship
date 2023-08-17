# Task 1 - Printing all names in ascending order

import pandas as pd

file1 = pd.read_excel("RESULT1.xlsx")
file2 = pd.read_excel("RESULT2.xlsx")

all_data = pd.concat([file1, file2])

names = all_data["NAME"]
print(names.sort_values(ignore_index=True))
