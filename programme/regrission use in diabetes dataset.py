import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets,linear_model
import numpy as np
from sklearn.metrics import mean_squared_error
dia=datasets.load_diabetes()#selecting data of diabetes checking from sklearn.dataset
#print(dia.keys()) find all the keys made in diabetes data and copy them
#dict_keys(['data', 'target', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])
''' data- it gives values of all feature
    target- it gives all labels
    feature_name- it gives heading of every feature'''
#x1=dia.feature_names()
x2=dia['data']
print(x2.shape)
x3=pd.DataFrame(x2,columns=dia['feature_names'])
print(type(x3))
print(x3)
#print(dia['data'])#it will give us whole data present in key value data(data of every feature)
print("##########################################################################################")
y1=dia.data[:,np.newaxis,2]#we are inserting column 2 in new axis called y1

print(x1)
'''x1_train=x1[0:5]#spliting data for training selecting only 5 rows
y1_train=dia.target[0:5]#spliting label for training first five data values
x2=dia.data[:,np.newaxis,2]
x1_test=x2[-5:]#spliting for testing selecting last 5 values for test
y1_test=dia.target[-5:]#spliting of testing
model=linear_model.LinearRegression()# using linearregression algo
model.fit(x1_train,y1_train)#apllying linear regression algo tao find  value of slope and one unknown so that best fited line can be figure out
y1_predict=model.predict(x1_test)#testing part nd storing predicted values in y so that it can be compared later with actual taget values
msv=mean_squared_error(y1_test,y1_predict)#compare both to find how much variation is there between two values
print(msv)
print("weights:",model.coef_)#  find value of one slope
print("intercepts:",model.intercept_)#fin value of unknown
plt.scatter(x1_test,y1_test)#graph of both test values
plt.plot(x1_test,y1_predict)#actual fited line by linear regression
plt.show()
'''
