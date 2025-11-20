import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import  StratifiedKFold
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay,precision_score, recall_score, f1_score
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV


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
df_clinico=pd.read_csv("historial_clinico.csv",sep=",")
#print(df_clinico.info())
#print(np.sum(df_clinico["fallecimiento"][df_clinico["fallecimiento"]==1]))
print(df_clinico["fallecimiento"].value_counts())


mantener = ["edad", "creatinina_fosfocinasa", "diabetes", "sangre_contraccion", 
            "plaquetas", "creatinina", "sodio", "seguimiento", 
            "anemia", "tension", "sexo", "fumador"]


X,y=filtrarDatos(df_clinico,mantener,"fallecimiento")
#print(X.shape)
#print(y.shape)

kf = StratifiedKFold(n_splits=3, shuffle=True)
modelo=SVC()

param_grid={"kernel":["rbf"],"gamma":[1,5,10],"C":[1,2,10]} # score de 1
#param_grid={"kernel":["sigmoid"],"gamma":[1,5,10],"C":[1,2,10]} #No adecuado
#param_grid={"kernel":["linear"]} #No muy bueno
#param_grid={"kernel":["poly"],"gamma":[1,5,10],"C":[1,2,10]} #No adecuado


gs = GridSearchCV(estimator=modelo, param_grid=param_grid, cv=kf, return_train_score=True)

gs.fit(X, y)

print("Mejor score:", gs.best_score_)
print("Mejores parámetros:", gs.best_params_)
# Puntajes de entrenamiento
print(gs.cv_results_['mean_train_score'][gs.best_index_])
# Puntajes de validación
print(gs.cv_results_['mean_test_score'][gs.best_index_])

#Creo el modelo con los mejores parámetros y entreno con todos los datos
modeloFinal=SVC(**gs.best_params_)
modeloFinal.fit(X,y)
y_pred=modeloFinal.predict(X)

precision = precision_score(y, y_pred)
recall_fallecidos = recall_score(y, y_pred)
recall_supervivientes=recall_score(y, y_pred, pos_label=0)
f1 = f1_score(y, y_pred)


print(f"Precisión: {precision}")
#Hago dos recall para ver la exhaustividad que hace cada modelo a fallecidos y supervivientes
print(f"Recall Fallecidos: {recall_fallecidos}")
print(f"Recall Supervivientes: {recall_supervivientes}")
print(f"F1-Score: {f1}")
print()

etiquetas = ["Superviviente", "Fallecido"]
cm = confusion_matrix(y, y_pred)
cmd = ConfusionMatrixDisplay(cm,display_labels=etiquetas)
cmd.plot(cmap='coolwarm')
plt.show()
print("-------------------------------------")