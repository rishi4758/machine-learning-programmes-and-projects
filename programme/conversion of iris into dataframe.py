from sklearn.datasets import load_iris
import pandas as pd
df=load_iris()
print(df.keys())
#x=df.drop(['feature_names'],1)
##################################### for using drop function convert data into data frame

d1=pd.DataFrame(df.data,columns=df.feature_names)
x=d1.drop(['sepal length (cm)'],1)
print(x)
print(d1.head())
d1=d1[['sepal width (cm)','sepal length (cm)']]
d1['mul']=(d1['sepal width (cm)']*d1['sepal length (cm)'])
#d1['mul']=(d1['sepal_length(cm)']*d1['sepal_width (cm)'])
print(d1)
