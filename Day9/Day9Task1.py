import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_excel("excel.xlsx")

rohit_runs = list(df["ROHIT"])
kohli_runs = list(df["KOHLI"])
dhawan_runs = list(df["DHAWAN"])
matches = np.arange(1, 8)

plt.bar(matches, rohit_runs, width=0.2, label='Rohit')
plt.bar(matches + 0.2, kohli_runs, width=0.2, label='Kohli')
plt.bar(matches + 0.4, dhawan_runs, width=0.2, label='Dhawan')

plt.xlabel('Matches')
plt.ylabel('Runs')
plt.title('Runs scored by Rohit, Kohli, and Dhawan in each match')
plt.legend()
plt.show()
