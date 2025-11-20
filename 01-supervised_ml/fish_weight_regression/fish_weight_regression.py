import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold,cross_validate
from sklearn.svm import SVR

def filtrarDatos(df:pd.DataFrame,mantener:list,datosY:str,eliminar:list=[]):
    #-----Si necesito eliminar columnas que no sirvan
    if eliminar:
        for columna in eliminar:
            del df[columna]
    #-----Si hay valores nulos 
    df=df.fillna(0)
    #-----Devuelve X e y para entrenar al modelo
    return df[mantener].values,df[datosY].values

#-----Cargo los datos
df_peces=pd.read_csv("acuario.csv",sep=",")
#print(df_peces.info())

X,y=filtrarDatos(df_peces,["Especie","Long_vert","Long_diag","Long_tras","Altura","Ancho"],"Peso")
#print(X.shape)
#print(y.shape)


kf = StratifiedKFold(n_splits=3, shuffle=True)

modelo=SVR()
#kf = KFold(n_splits=3, shuffle=True)

#param_grid=[{"kernel":["rbf","linear","sigmoid"],"gamma":[1,5,10],"epsilon":[0.2,1,3,10],"C":[1,2,10]},{"kernel":["poly"],"gamma":[1,5,10],"epsilon":[0.2,1,3,10],"C":[1,2,10]}]
param_grid=[{"kernel":["rbf","linear","sigmoid"],"gamma":[1],"epsilon":[42,44,48,50,60],"C":[1]}]


gs = GridSearchCV(estimator=modelo, param_grid=param_grid, cv=kf.split(X, df_peces["Especie"]), return_train_score=True)

gs.fit(X, y)#Dentro de gs se dividen los datos

#El score de best_score aunque sea el mejor score para esos parametros va a ser igual al score del test ya que se basa en ese score para elegir los parámetros más obtimos
print("Mejor score:", gs.best_score_)
print("Mejores parámetros:", gs.best_params_)
# Puntajes de entrenamiento
print(gs.cv_results_['mean_train_score'][gs.best_index_])
# Puntajes de validación
print(gs.cv_results_['mean_test_score'][gs.best_index_])

"""
#Ahora veo si el score del modelo con estos parámetros(No hace falta ya que grid searh devuelve el score de entrenamiento y test)
scoreSVR=cross_validate(modeloFinal,X,y,cv=kf.split(X, df_peces["Especie"]),return_train_score=True)
print("-------Score SVR Lista-------")
print(scoreSVR["train_score"])
print(scoreSVR["test_score"])
print()"""


#Creo un modelo SVR con los mejores parámetros
modeloFinal = SVR(**gs.best_params_)
#Una vez que se que el modelo es bueno lo entreno con todos los datos
modeloFinal.fit(X,y)
print("Prediccion:")
print(modeloFinal.predict([[0,29.4,32,37.2,14.65,5.17]]))

