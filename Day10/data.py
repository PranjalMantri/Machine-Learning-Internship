import  pandas as pd
from matplotlib import pyplot as plt

file1 = pd.read_excel("RESULT1.xlsx")
file2 = pd.read_excel("RESULT2.xlsx")

alldata = pd.concat([file1, file2])
print(alldata)
print(alldata["NAME"])

name = list(alldata["NAME"])
total = list(alldata["TOTAL"])

print(alldata.head(3))
print(alldata.tail(3))

print(alldata.sort_values(["TOTAL"], ascending=False, kind='quicksort', inplace=False))

plt.bar(name, total)
plt.show()
