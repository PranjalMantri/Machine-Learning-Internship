


import pandas as pd
from sklearn import linear_model

df = pd.read_csv("data.csv")
print(df)

reg = linear_model.LinearRegression()
reg.fit(df[["x1", "x2"]], df[["y"]])
print(reg.predict([[13, 11]]))
print(reg.coef_)
print(reg.intercept_)
