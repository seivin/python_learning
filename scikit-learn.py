from sklearn import neighbors, datasets, preprocessing
from sklearn.metrics import accruacy_score
from sklearn.cross_validation import cross_val_score

import numpy as numpy

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)

from sklearn.preprocessing import Normalizer
scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)

from sklearn.preprocessing import Binarizer
binarizer = Binarizer(threshold=0.0).fit(X)
binary_X = binarizer.transform(X)

# Linear Regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression(normalize=True)
lr.fit(X, y)  # Model fitting
y_pred = lr.predict(X_test)
print(cross_val_score(lr, X, y, cv=2))

  # Regression metrics
  from sklearn.metrics import mean_absolute_error
  y_true = [3, -0.5, 2]
  mean_absolute_error(y_true, y_pred)

  from sklearn.metrics import mean_squared_error
  mean_squared_error(y_test, y_pred)

  from sklearn.metrics import r2_score
  r2_score(y_true, y_pred)

# K-NN (example)
from sklearn import neighbors
iris_dataset = datasets.load_iris()
X, y = iris_dataset.data[:, :2], iris_target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33)
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict_proba(X_test)
accruacy_score(y_test, y_pred)

  # knn.score(X_test, y_test)
  # print(cross_val_score(knn, X_train, y_train, cv=4))

# SVM
from sklearn.svm import SVM
svc = SVC(kernel='linear')
svc.fit(X_train, y_train)

# Naive Bayes
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()