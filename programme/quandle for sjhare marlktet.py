#import pandas as pd

import quandal
import pandas as pd

d=Quandal.get('WIKI/GOOGL')
print(d.head())











import numpy as np
'''s=np.array([[89,95,78],[65,89,78],[56,32,78]])
print(s)
x=pd.DataFrame(s,columns=['math','physics','chemistry'])
f=['math','physics','chemistry']
c={'data':x,'feature':f}
z=pd.DataFrame(c)
pd.DataFrame(z.to_csv("marks4.csv"))
'''
'''
b=pd.read_csv("marks4.csv")
print(b.data.T)
'''
