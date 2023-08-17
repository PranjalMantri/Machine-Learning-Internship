# Task 2 - Generate Merit and store it in Matrix.xlsx file

import pandas as pd

file1 = pd.read_excel("RESULT1.xlsx")
file2 = pd.read_excel("RESULT2.xlsx")

all_data = pd.concat([file1, file2])

topper = all_data.sort_values(["TOTAL"], ascending=False).head(3)
topper.to_excel("Matrix.xlsx", index=False)
