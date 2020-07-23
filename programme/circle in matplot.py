import numpy as np

x1=np.array([[1,2,3],[0,6,4],[5,2,8]])
mu=x1.mean()
std=x1.std()
xs=(x1-mu)/std
o=np.hstack(x1)
v=list(o)
for i in range(len(v)):
  print(v[i])
  if(v[i]>1):
    v.remove(i)
  #i=0
    

