import pandas as pd

mydata = [100, 233, 200]
print(mydata)
pddata = pd.DataFrame([100, 233, 200], index=["First", "Second", "Third"])
print(pddata)

data1 = (10, 20, 30, 40, 50)
pddata1 = pd.DataFrame(data1)
print(pddata1)

dictdata = {"A": [30], "B": [40], "C": [20]}
pddictdata = pd.DataFrame(dictdata)
print(pddictdata)

dictdata2 = pd.DataFrame([[10, 20, 30], [40, 50, 50, 60], [70, 80, 90]])
print(dictdata2)

dictdata3 = pd.DataFrame(
    [["Rohit", "Batsman", 50], ["Bumrah", "Bowler", 65], ["Dhoni", "Batsman", 100]],
    columns=["Name", "Type", "Run"],)

print(dictdata3)
print(dictdata3["Name"][1])

jobframe = pd.DataFrame([[10000, 15000, 17000], [25000, 30000, 32000]], columns=[2020, 2021, 2022], index=["abc", "xyz"])
print(jobframe)

jobframe[2023] = jobframe[2022] + (15 * (jobframe[2022] / 100))
jobframe["total"] = 12 * (jobframe[2020] + jobframe[2021] + jobframe[2022] + jobframe[2023])
print(jobframe)
