from sklearn import linear_model
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,accuracy_score
import pickle
s=load_iris()
#oh=to_categorical(s['target'])
train_x,test_x,train_y,test_y=train_test_split(s['data'],s['target'],test_size=0.3)#30 percent of total dataa is for testing
print(s['data'].shape)
print(test_y.shape)
print(type(s['data']))

'''model=linear_model.LinearRegression()
model=model.fit(train_x,train_y)#pickle is used if we do not want to train our data again and again because its a time wastage so once training model westore it in pickle file sot that when we need trained data we can use that file
with open('ram.pickle','wb') as r:
  pickle.dump(model,r)'''
s1=open('ram.pickle','rb')
model=pickle.load(s1)
y_predict=model.predict(test_x)
msv=mean_squared_error(test_y,y_predict)#compare both to find how much variation is there between two values
print(msv)
print(y_predict.shape,test_y.shape)
#accuracy_score(np.array(test_y),np.array(y_predict))
import matplotlib.pyplot as plt
plt.plot(test_x,y_predict)
plt.show()
plt.plot(test_x,test_y)#
plt.show()
