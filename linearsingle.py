import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
student = pd.read_csv('student_scores.csv')
print("SJC2MCA-2027 Georgekutty Biju\nS3MCA")
print(student.head())
student.describe()
student.info()
X = student.iloc[:, :-1].values
y = student.iloc[:, -1].values
Xax = student.iloc[:, :-1]
Yax = student.iloc[:, -1]
plt.scatter(Xax, Yax)
plt.xlabel("No. of hours")
plt.ylabel("Score")
plt.title("Student scores")
plt.show()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print('INTERCEPT=', regressor.intercept_)
print('COEFFICIENT=', regressor.coef_)
y_pred = regressor.predict(X_test)
for i, j in zip(y_test, y_pred):
    if i != j:
        print("Actual value:", i, "Predicted value:", j)
print("Number of mislabeled points from test data set :", (y_test != y_pred).sum())
print("Mean Absolute error :", metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared error :", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared error :", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))