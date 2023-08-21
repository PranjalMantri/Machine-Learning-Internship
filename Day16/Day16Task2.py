

import pandas as pd
from sklearn import linear_model

df = pd.read_csv("sales_data.csv")
print(df)

reg = linear_model.LinearRegression()
reg.fit(df[["money"]], df[["sales"]])
print(reg.predict([[5]]))
print(reg.coef_)
print(reg.intercept_)
