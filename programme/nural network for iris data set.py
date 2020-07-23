from sklearn.datasets import load_iris
import numpy as np
from tensorflow import keras
from  keras.utils import to_categorical   # used for onr hot encoding
from sklearn.model_selection import train_test_split
iris = load_iris()
iris.keys()
iris['target'][:5]
np.unique(iris['target'])
target_oh = to_categorical(iris['target'], 3)
'''X_train, X_test, y_train, y_test = train_test_split(iris['data'], 
                                                     target_oh,
                                                    test_size = 0.2)'''
X_train=iris.data[:5]
y_train=iris.target[:5]
X_test=iris.target[-5:]
y_test=iris.target[-5:]
mean = np.mean(X_train, axis = 0)
std = np.std(X_train, axis = 0)

X_train_n = (X_train - mean)/(std+0.000000001)
X_test_n = (X_test - mean)/(std+0.000000001)
from keras.layers import Input, Dense
from keras.models import Model
from keras import optimizers


input_layer = Input(shape=(4, ))
hidden_layer_1 = Dense(10, activation = 'sigmoid')(input_layer)
hidden_layer_2 = Dense(5, activation = 'sigmoid')(hidden_layer_1)
output_layer = Dense(3, activation = 'sigmoid')(hidden_layer_2)

model = Model(inputs = [input_layer, ], outputs = [output_layer])
model.compile(loss = 'mse', optimizer = optimizers.SGD(lr=0.1), 
              metrics = ['accuracy',])
model.fit(X_train_n, y_train, batch_size = 10, epochs = 1000, 
          validation_split = 0.1)
