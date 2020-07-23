
import numpy as np
'''def minor(arr,i,j):
    # ith row, jth column removed
#    return arr[np.array(list(range(i))+list(range(i+1,arr.shape[0])))[:,np.newaxis],
#            np.array(list(range(j))+list(range(j+1,arr.shape[1])))]


'''


#for 1st row 1st column01
s=np.array([[1,2,3],[4,5,6],[7,8,9]])
b1=s[np.array([1,2])[:,np.newaxis],np.array([[1,2],[0,2]])]#if each row has difeernt column values

b=s[np.array([1,2])[:,np.newaxis],np.array([1,2,0])]
print(b)
print(b1)
#print(minor(s,0,0))
