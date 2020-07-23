import pandas as pd
s=[[1,2,3,4],[5,6,7,8],[1,2,3,4],[15,16,17,18],[12,32,33,34],[45,56,67,68]]
b=pd.DataFrame(s,columns=['name','age','number','years'])
c=b[['name','age']]
print(b)
print("################################## to select some columns#################################")
print(c)
print("################################# using head first five function##################################")
print(b.head())

print("############################# using tail last five function######################################")
print(c.tail())
print("################################## to select some 4th rows from column#################################")
print(c['age'][4])
print("################################## print some rows of  specific column#################################")
for i in range(0,3):
  print(c['age'][i])
