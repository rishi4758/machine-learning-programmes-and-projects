from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
da=datasets.load_iris()
print(da.keys())
print(da.DESCR)
s1=da.data
s2=da.target
model=KNeighborsClassifier()
model.fit(s1,s2)
y1=model.predict([[4,5,6,7]])
print(y1)
