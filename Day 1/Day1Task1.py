# Task 1

myData = {"Maharashtra": {"Mumbai": {"City": "Metro City", "Metro": "Yes"},
                           "population": "20 Cr."},
          "Gujarat": ["Ahmedabad", "Surat", "Rajkot"],
          "Rajasthan": ["Ajmer", "Jaipur", {"Capital": "Jaipur"}, ["Mewad", "RJ", "INR"]]
          }

print(myData["Maharashtra"]["Mumbai"]["City"])
print(myData["Rajasthan"][1])
print(myData["Gujarat"][2])
print(myData["Rajasthan"][3][1])
