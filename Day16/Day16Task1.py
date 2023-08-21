# import pandas as pd
# from sklearn import linear_model
#
# df = pd.read_csv("car_data.csv")
# print(df)
#
# reg = linear_model.LinearRegression()
# reg.fit(df[["car_age"]], df[["price"]])
# print(reg.predict([[2]]).round(2))
# print(reg.coef_.round(2))
# print(reg.intercept_.round(2))

import time
import matplotlib.pyplot as plt
import pandas as pd

file = "sales_data.csv"
df = pd.read_csv(file)
data = df["money"].tolist()
data1 = df["sales"].tolist()
xbar = 0
ybar = 0


def bar(a):
    n = len(a)
    sigma = 0
    for i in a:
        sigma += i
    return sigma / n
def sum(a):
    sigma=0
    for i in a:
        sigma+=i
    return sigma
def bars(sum,xbar):
    values = []
    for x in sum:
        value = x - xbar
        values.append(value)
    return values
def anysquare(b,c):
    values = []
    for x in range(len(b)):
        value = b[x]*c[x]
        values.append(value)
    return values
def calculate_b1(sumation_xy,sumation_x2):
    numerator = sumation_xy
    denominator = sumation_x2
    b1 = numerator / denominator
    return b1
def calculate_b0(yar,xbar,b1):
    x = b1 *xbar
    final = yar-x
    return final
def lrpr(uservalue,b1,b0):
    value = b0 + (b1*uservalue)
    return value

xbar=bar(data)
print(xbar)
ybar=bar(data1)
print(ybar)
xxbar=bars(data, xbar)
print(xxbar)
yybar=bars(data1, ybar)
print(yybar)
bothsummation=anysquare(xxbar,yybar)
print(bothsummation)
x2summation=anysquare(xxbar,xxbar)
print(x2summation)
xy=sum(bothsummation)
print(xy)
x2=sum(x2summation)
print(x2)
b1_result = calculate_b1(xy,x2)
print("b1 =", b1_result)
b0_result = calculate_b0(ybar, xbar, b1_result)
print("b0 =", b0_result)
#change here when you run the code
userinput=14
fvalue=lrpr(userinput,b1_result,b0_result)
print("predicted value=",fvalue)
columnsnmae = df.columns.tolist()
cname =""
rname =""
adddata=0
for i in columnsnmae:
    if i=="sales":
        cname = i
        userinput = 423
    elif i == "CarAge":
        cname =i
        userinput = 14
    elif i == "area":
        cname = i
        userinput = 3300
    elif i == "Price":
        rname = i
        adddata = fvalue
    elif i == "dollars":
        rname = i
        adddata = fvalue
    else:
        print("wrong data")
new_data=pd.DataFrame({cname: [userinput],
                       rname: [adddata]})
# combined_data = pd.concat([df,new_data],ignore_index=True)
# combined_data.to_csv(file,index=False)
time.sleep(5)
file1="sales_data.csv" #change here when you run the code
df=pd.read_csv(file1)
plt.scatter(df.money, df.sales) #change here when you run the code
plt.show()