import numpy as np
########### conversion of list into np array
a=[[1,2,3,4,4],[2,3,4,5,6]]
s=np.array(a)
print(s)
############### conversion of np array to list
f=np.array([[1,2,3],[4,5,6],[12,15,18]])
v=np.hstack(f)
a1=list(v)
print(a1)
