from matplotlib import pyplot as plt

dhoni = [45, 78, 43, 99]
kohli = [100, 22, 44, 66]
rohit = [34, 56, 88, 11]
matches = [1, 2, 3, 4]

plt.scatter(matches, dhoni, label = "Dhoni")
plt.scatter(matches, kohli, label = "Kohli")
plt.scatter(matches, rohit, label = "Rohit")
plt.legend()
plt.show()
