import pandas as pd
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
import random

distance=[]

def knn(data,predict,k):
    for i in data:
        for s in data[i]:
            di=np.sqrt(np.sum((np.array(s)-np.array(predict))**2))
            distance.append([di,i])
    s= [j[1] for j in sorted(distance) [:k]]     
    print(s)
    print(Counter(s))
    print(Counter(s).most_common(1))
    print(Counter(s).most_common(1)[0][0])
    x=Counter(s).most_common(1)[0][0]
    #y=Counter(s).most_common(1)[0][1] for confidence
    return x


df=pd.read_csv("breast-cancer-wisconsin.data")
df.replace('?',-9999,inplace=True)
df=df.drop(['id'],1)
test_size=0.2
df=df.astype(float).values.tolist()
random.shuffle(df)
train_x=df[:-int(test_size*len(df))]
test_x=df[-int(test_size*len(df)):]
tr_set={2:[],4:[]}
test_set={2:[],4:[]}
c=0
t=0
for i in train_x:
   tr_set[ i[-1]].append(i[:-1])

for x in test_x:
    test_set[x[-1]].append(x[:-1])
for group in test_set:
    for data in test_set[group]:      
        s=knn(tr_set,data,5)
        print(group)
        if group==s:
            c+=1         
        t+=1
print(c,t)
print("accuracy",c/t)

'''
p=  {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_point=[1,6]
#print(knn(p,new_point,3))
for i in p:
    for a in p[i]:
        plt.scatter(a[0],a[1],s=100,color=i)
plt.scatter(new_point[0],new_point[1],s=50,color=knn(p,new_point,3))
plt.show()

x={'s':[[1,2],[3,4],[3,1]],'r':[[7,8],[6,3],[8,6]]}
for i in x:
    print(i)
    for z in x[i]:
        print(z)
'''
