# Task 2 - Basic Dictionary Accessing

myData = {"Category": [{"A": "FIRST", "Package": {"Data": "2 Lacs"}},
                       {"B": "Second", "Data": {"New": [100]}},
                       {"C": "Third", "Tests": [45, 75, 25]}]}

print(myData["Category"][0]["Package"]["Data"])
print(myData["Category"][2]["Tests"][2])
print(myData["Category"][1]["Data"]["New"][0])
