import pandas as pd

file = "excel.xlsx"
filedata = pd.read_excel(file)
print(filedata)
print(filedata["KOHLI"])
