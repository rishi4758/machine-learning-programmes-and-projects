import numpy as np
s=np.array([[2,3,"rishav",5],[1,2,34,0]])
print(s.shape)
print(s)
print(np.zeros([1,3]))# defsult is float vslue thid is single row with three column
print(np.zeros([3,4],dtype=int))#conversion in int datatype
print(np.ones(3,))
x9=np.zeros([6,7])
x5=np.ones([6,10],dtype=int)
print(x5)
########### insert delete concatenate operation in numpy
x=np.array([2,3,4,5])
print(x)
x1=np.append(x,[89,90])
print(x1)
x2=np.delete(s,7)# araay with index number
print(x2)
s1=np.concatenate((x,np.array([3,4,5,6])),axis=0)#inside concatenate we always use tuple
s4=np.array([[2,3,"rishav",5],[1,2,34,0]])
print(x5[1:2])#printing number of rows with all columns
#printing number of specific columns specific rows
for i in range(4):
    print(x5[i,...,4:8])#for chosing any rows and slicing its columns
print(x9[...,2,2:6])#for chossing any column and slicing its rows 
