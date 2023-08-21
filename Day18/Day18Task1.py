# Random Forest

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("titanic.csv")
data.dropna()
x = data.drop(["Name", "Sex", "Embarked", "Ticket", "Cabin", "Age", "Survived"], axis=1)
y = data["Survived"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=20)
rf_classifier.fit(x_train, y_train)
predictions = rf_classifier.predict(x_test)
accuracy = accuracy_score(y_test, predictions)

print(accuracy)
