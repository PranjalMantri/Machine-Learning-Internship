# Pie Chart

from matplotlib import pyplot as plt

branches = ["CE","IT", "ME", "EC", "ICT", "CIVIL", "BIOMEDICAL"]
seats = [120, 60, 45, 45, 30, 50, 20]

plt.pie(seats, labels = branches, explode=(0.2, 0, 0, 0, 0, 0, 0), shadow=False, autopct="%1.2f%%")
plt.show()