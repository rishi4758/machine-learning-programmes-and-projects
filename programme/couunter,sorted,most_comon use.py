import numpy as np
from collections import Counter
#a=np.array([1,2,312])
b=np.array([7,1,6,7,8,9,1,1,2,6])
#c=a-b
print(sorted(b))# it will sort
print(Counter(b))#it willcount the occurence gives in form of keys and values
print(Counter(b).most_common(2))# it will find the 2 most occuring values with keys
print(Counter(b).most_common(1)[1][0])# it will print the perticular value or key on the basis of index
    
