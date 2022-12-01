from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import numpy as np

#Database
#x = data, y = target
x = [[i] for i in range(10)]
y = [i ** 3 for i in range(10)]

print(x)
print(y)