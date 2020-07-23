

import numpy as np
def yoh(l):
  s=len(l)
  k=np.zeros([s,s])
  for i in range(0,s):
    k[i,i]=1
  return k
label=np.array(['cat','dog','mouse'])
print(yoh(label))
