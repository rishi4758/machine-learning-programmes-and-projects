import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import svm
style.use('ggplot')
a={'1':np.array([[1,2],[2,3],[2,5]]),'0':np.array([[6,5],[7,3],[6,9]])}
def class mongo:
    def __init__(self,visualization=True):
        self.colors={1:'r',0:'k'}
        if self.visualization:
            self.fig=plt.figure()
            self.ax=self.fig.add_subplot(1,1,1)



    def fit(self,data):
        pass


    def predict(self,features):# we use sign function because its graph will give us either 1 or 0 to seperate the data

        s=np.sign(np.dot(np.array(features),self.w)+self.b)
        return s




    
