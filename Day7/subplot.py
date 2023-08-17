# Subplot

from matplotlib import pyplot as plt

time = ["9:00", "9:30", "10:00", "10:30", "11:00","11:30", "12:00"]
bob = [180, 176, 182, 187, 90, 95, 100]
sbi = [25, 66, 100, 122, 123, 220, 200]
hdfc = [100, 122, 111, 133, 55, 66, 33]

plt.subplot(1, 3, 1)
plt.plot(time, bob)
plt.title("BOB")

plt.subplot(1, 3, 2)
plt.plot(time, sbi)
plt.title("SBI")

plt.subplot(1, 3, 3)
plt.plot(time, hdfc)
plt.title("HDFC")

plt.show()

