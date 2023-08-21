

import pandas as pd
from sklearn import linear_model

df = pd.read_csv("prices.csv")
print(df)

reg = linear_model.LinearRegression()
reg.fit(df[["area"]], df[["price"]])
print(reg.predict([[2400]]))
print(reg.coef_)
print(reg.intercept_)
