import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
import numpy as np
s=np.array([[1,2,3],[5,6,7]])
x=pd.DataFrame(s,columns=["length","breadth","height"])
s=x["length"]*x["breadth"]*x["height"]
feature=[[s[0]],[s[1]]]
label=["cube","cuboid"]
c=linear_model.LinearRegression(feature,label)
c=c.fit(feature,label)
plt.plot(feature,label,c)
plt.show()
