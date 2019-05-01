import pandas as pd
import numpy as np
import quandl
import math
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100.0
df['PCT_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100.0

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']] #features

#print(df.head())

forecast_col = 'Adj. Close'
df.fillna(-99999,inplace=True)
forecast_out = int(math.ceil(0.01*len(df))) #ceil redondea, predecir 10% del data frame

df['label'] = df[forecast_col].shift(-forecast_out) #se mueve a +10 dias en el futuro
df.dropna(inplace=True)
#print(df.head())

X = np.array(df.drop(['label'],1))
Y = np.array(df['label'])

X = preprocessing.scale(X) #escalar con todos los otros valores OJO añade tiempo de procesamiento
Y = np.array(df['label'])

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y,test_size=0.2) #20% de los datos, los mueve manteniendo los valores y output los valores calculados

clf = LinearRegression(n_jobs=-1) #njobs es el numero de trabajos utilizados para los calculos, -1 es para utilizar todos los CPUS, incrementar esto ayuda a la velocidad
clf.fit(X_train,Y_train)
accuracy = clf.score(X_test,Y_test) #se esta haciendo con 2 datos, asi no sabe los valores
print('>>Accuracy LinearRegression:',accuracy) #es igual al error al cuadrado

clf2 = svm.SVR() #support vector regression
clf2.fit(X_train, Y_train)
accuracy2 = clf2.score(X_test,Y_test)
print('>>Accuracy SVM SVR:',accuracy2)

clf3 = svm.SVR(kernel='poly')
clf3.fit(X_train,Y_train)
accuracy3 = clf3.score(X_test,Y_test)
print('>>Accuracy SVM SVR Kernel Polynomial:',accuracy3)



