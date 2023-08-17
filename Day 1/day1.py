# Basics of Dictionaries
# Dictionary Rules
# Curly Brackets {}
# Key Value Pair {Key : Value}

myData = {"Ahmedabad": "Gujarat"}
print(myData)
print(myData["Ahmedabad"])

myData1 = {"Ahmedabad": "Gujarat", "Jaipur": "Rajasthan", "Bhopal": "MP"}
print(type(myData1))
print(myData1["Jaipur"])

myData2 = {"Ahmedabad": 500, "Surat": 400, "Rajkot": 300}
print(myData2["Rajkot"])

myData3 = {"Ahmedabad": 500, "Surat": [400, 200, 10]}
print(myData3["Surat"][2])
