from matplotlib import pyplot as plt

dhoni = [45, 78, 43, 99]
kohli = [100, 22, 44, 66]
rohit = [34, 56, 88, 11]
matches = [1, 2, 3, 4]

plt.plot(matches, dhoni, label = "Dhoni")
plt.plot(matches, kohli, label = "Kohli")
plt.plot(matches, rohit, label = "Rohit")
plt.legend()
plt.show()
