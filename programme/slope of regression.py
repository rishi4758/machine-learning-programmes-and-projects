import numpy as np
from sklearn import linear_model
xs=np.array([1,2,3,4,5,6])

y_original=np.array([5,4,6,5,6,7])
def slope(xs,y_original):
    m=((np.mean(xs)*np.mean(y_original))-np.mean(xs*y_original))/((np.mean(xs)*np.mean(xs))-np.mean(xs*xs))
    return m
print("slope",slope(xs,y_original))
'''xs=xs.reshape(-1,1)
x1_train=xs[:3]
x1_test=xs[3:]
y1_train=y_original[:3]
y1_test=y_original[3:]
model=reg_linear_model.reg_linearRegression()
model.fit(x1_train,y1_train)
pre=model.predict(x1_test)
'''


m=slope(xs,y_original)
def intercept(y_original,xs,m):
  return ((np.mean(y_original))-(m*np.mean(xs)))
print("intercept",intercept(y_original,xs,m))
c=intercept(y_original,xs,m)
reg_line=[]
for i in xs:
    reg_line.append(m*i+c)
def sos(y_l,y_o):
    return sum((y_l-y_o)**2)


def accuracy(y_o,y_l):
    y_o_mean=np.mean(y_o)
    
    squared_reg_line=sos(y_l,y_o)
    squared_y_o=sos(y_o,y_o_mean)
    return 1-(squared_reg_line/ squared_y_o)

print("accuracy",accuracy(y_original,reg_line)) 
#np.array([m*x+c,for x in xs])

import matplotlib.pyplot as plt
#plt.scatter(xs,y_original)
#plt.plot(xs,y_original)
plt.scatter(xs,y_original)
plt.plot(xs,reg_line)
plt.show()

