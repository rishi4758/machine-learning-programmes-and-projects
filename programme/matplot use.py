import matplotlib.pyplot as plt
x1=[1,2,3]#point on x-axis
y1=[15,25,35]#point on y axis of coresponding x-axis
x2=[11,12,13]
y2=[35,40,45]
'''### for line chart use plt.plot
plt.plot(x1,y1,label='milk',color="black")# for ploting x1 and y1 values
plt.plot(x2,y2,label='bread',color='red')
###### for bar chart use plt.bar 
plt.bar(x1,y1,label="dudh ka bar chart",color="green")
plt.bar(x2,y2,label="bread ka bar chart",color="red")'''
#### FOR SCATTER chart use plt.scater
plt.scatter(x1,y1,label="dudh",marker="x",color="red")
plt.scatter(x2,y2,label="bread",marker="<",color="black",s=62)# s for size
plt.xlabel("days")
plt.ylabel("price in rupee")
plt.title("dudh bread ka graph")
plt.legend()
plt.show()

