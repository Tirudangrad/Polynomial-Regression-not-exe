import numpy as np
from sklearn.linear_model import LinearRegression

#Database
# x = data, y = target
x = [[1],[3],[5],[7],[9]]
y = [2,6,10,14,18]

regr = LinearRegression().fit(x,y)
regr.score(x, y)




#data uji
predict = np.array([[10]])

#menampilkan data prediksi
print ("prediksi")
print ("Input = ", predict)
print ("output = ", regr.predict(predict))
