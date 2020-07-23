import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
import numpy as np


s=pd.read_csv('breast-cancer-wisconsin.data')
s.replace('?',-9999,inplace=True)
k=s.drop(['id'],1)
full_data=k.astype(float).values.tolist()
print(full_data)



s=s.drop(['id'],1)
inputs=np.array(s.drop(['classes'],1))
outputs=np.array(s['classes'])
x_train,x_test,y_train,y_test=train_test_split(inputs,outputs,test_size=0.2)
model=svm.SVC()
model=model.fit(x_train,y_train)
y=model.predict(x_test)
accuracy=model.score(x_test,y_test)
print(accuracy)
a1=model.score(x_test,y)
print(a1)
