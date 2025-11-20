import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_validate, GridSearchCV
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split,ShuffleSplit
from sklearn.metrics import mean_squared_error, r2_score

# Cargar los datos
df = pd.read_csv("bike_rentals.csv")

#Ver columnas
print(df.columns)

#Ver nulos
print(df.isna().sum())

#Borrar columans
df = df.drop(columns=["instant","mnth","weekday","holiday","hum","atemp"]) 

for i in df.columns:
    print(df[i].value_counts())
    print("------------------")

#Aplico one hot en las columnas de más de dos value_counts
df = pd.get_dummies(df, columns=['weathersit',"season"])

# Ver cuántas bicicletas se alquilaron en total por año
total = df.groupby('yr')['cnt'].sum()
print("Total de bicicletas alquiladas por año:")
print(total)
print()



#Codifico las columnas que tienen dos valores
cod_workingday = df['workingday'].factorize()[1] 
df['workingday'] = df['workingday'].factorize()[0]

cod_yr = df['yr'].factorize()[1] 
df['yr'] = df['yr'].factorize()[0]

#Escalo las columnas numéricas
scaler = MinMaxScaler()
columns_to_scale = ["temp","windspeed","cnt",]
df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

#print(df.describe())
#for i in df.columns:
#    print(df[i].value_counts())
#    print("------------------")

#Asigno X e Y
X=df.drop(columns="cnt").values
y=df["cnt"].values



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,shuffle=True)



#LinearRegression y Polynomial

print("-----LinearRegression-----")
modeloLineal=LinearRegression()
modeloLineal.fit(X_train,y_train)
print(f"Test Score: {modeloLineal.score(X_test,y_test)}")
print()

"""
kf=KFold(n_splits=3, shuffle=True)
modeloLineal3=LinearRegression()
scoreL=cross_validate(modeloLineal3,X,y,cv=kf,return_train_score=True)
print("-------Score LinealRegression Media-------")
print(np.mean(scoreL["train_score"]))
print(np.mean(scoreL["test_score"]))
print()
"""

print("-----PolynomialRegression-----")
modeloLineal2=LinearRegression()
pf=PolynomialFeatures(degree=2)
X_Pol_train=pf.fit_transform(X_train)
X_Pol_test=pf.transform(X_test)
modeloLineal2.fit(X_Pol_train,y_train)
print(f"Test Score: {modeloLineal2.score(X_Pol_test,y_test)}")
print()



#SVR

kernels = ['linear', 'poly', 'rbf', 'sigmoid']
for kernel in kernels:
    print(f"-----SVR {kernel} Kernel-----")
    svrM = SVR(kernel=kernel, degree=3, gamma='scale', C=1.0, epsilon=0.1)
    
    svrM.fit(X_train, y_train)

    y_pred = svrM.predict(X_test)
    print(f"Test Score: {svrM.score(X_test,y_test)}")
    print("-------------------------")
    print()