import numpy as np
import pandas as pd
from tensorflow.keras.layers import Dense,Input
from sklearn.datasets import load_iris
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.models import Model
from keras import optimizers


s=load_iris()
oh=to_categorical(s['target'],3)
tr_x,te_x,tr_y,te_y=train_test_split(s['data'],oh,test_size=0.5)
i=Input(np.shape(tr_x))
h1=Dense(5,activation='sigmoid')(i)
h2=Dense(3,activation='sigmoid')(h1)
o=output=Dense(3,activation='sigmoid')(h2)
model=Model(inputs=[i,],outputs=[o])
model.compile(loss='mse',optimizer=optimizers.SGD(lr=0.5),metrics='accuracy')
model.fit(tr_x,tr_y,batch_size=3,epochs=4,validation_split=0.1)
