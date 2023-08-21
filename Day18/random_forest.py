# Random Forest

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

file_data = pd.read_csv("diabetes.csv")

x = file_data.drop("Outcome", axis=1)
y = file_data["Outcome"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

rfclassifier = RandomForestClassifier(n_estimators=50, random_state=0)
rfclassifier.fit(x_train, y_train)
predictions = rfclassifier.predict(x_test)
accuracy = accuracy_score(y_test, predictions)

print(accuracy)