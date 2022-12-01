from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import numpy as np

#Database
#x = data, y = target
x = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
y = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

#Data uji
predict = np.array([[11]])
poly = PolynomialFeatures(degree=3)
x_ = poly.fit_transform(x)
predict_ = poly.fit_transform(predict)
regr = linear_model.LinearRegression()
regr.fit(x_,y)

#Menampilkan data prediksi
print("Prediksi")
print("Input = ", predict)
print("Output = ", regr.predict(predict_))