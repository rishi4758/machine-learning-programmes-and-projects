import numpy as np
def minor(A, i):
    x=A[0]
   
    if i==0:
        return A[np.array(list(range(1,A.shape[0])))[:,np.newaxis],np.array(list(range(i))+list(range(i+1,A.shape[1])))]
    if i==1:
        return A[np.array(list(range(1,A.shape[0])))[:,np.newaxis],np.array(list(range(i))+list(range(i+1,A.shape[1])))]
    
    if i==2:
        return A[np.array(list(range(1,A.shape[0])))[:,np.newaxis],np.array(list(range(i))+list(range(i+1,A.shape[1])))]
    


a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(minor(a,2))
