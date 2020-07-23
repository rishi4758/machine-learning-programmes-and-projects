  
import numpy as np
x1=np.array([[1,2,3],[2,3,4],[5,67,8]])
th=2
for i in x1:
  if(any(i>th)):### read it like any of i is greater than th
    print("hello")
