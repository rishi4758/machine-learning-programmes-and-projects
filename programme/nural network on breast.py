import pandas as pd
from sklearn.model_selection import train_test_split
from keras.layers import Input ,Dense
from keras.models import Model
from keras import optimizers
import numpy as np


s=pd.read_csv('breast-cancer-wisconsin.data')
s.replace('?',-9999,inplace=True)
k=s.drop(['id'],1)
full_data=k.astype(float).values.tolist()
#print(full_data)



s=s.drop(['id'],1)
inputs=np.array(s.drop(['classes'],1))
outputs=np.array(s['classes'])
x_train,x_test,y_train,y_test=train_test_split(inputs,outputs,test_size=0.2)

input_layer = Input(shape= x_train[0].shape)
hidden_layer_1 = Dense(10, activation = 'sigmoid')(input_layer)
hidden_layer_2 = Dense(5, activation = 'sigmoid')(hidden_layer_1)
output_layer = Dense(1, activation = 'sigmoid')(hidden_layer_2)

model = Model(inputs = [input_layer, ], outputs = [output_layer])
model.compile(loss = 'mse', optimizer = optimizers.SGD(lr=0.1), 
              metrics = ['accuracy',])
s=model.fit(x_train, y_train, batch_size = 10, epochs = 10, 
          validation_split = 0.1)
#pre=model.predict(x_test)
accuracy=s.score(x_test,y_test)
print(accuracy)
