from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import  StratifiedKFold, cross_validate
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay,precision_score, recall_score, f1_score
from sklearn.tree import plot_tree


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
#print(df_clinico["fallecimiento"].value_counts())


mantener = ["edad", "creatinina_fosfocinasa", "diabetes", "sangre_contraccion", 
            "plaquetas", "creatinina", "sodio", "seguimiento", 
            "anemia", "tension", "sexo", "fumador"]


X,y=filtrarDatos(df_clinico,mantener,"fallecimiento")
#print(X.shape)
#print(y.shape)

kf = StratifiedKFold(n_splits=5, shuffle=True)

#Hay que poner los parámetros correctos para conseguir un buen score
arbol = DecisionTreeClassifier(criterion='gini',max_depth=5, min_samples_split=10, min_samples_leaf=5,class_weight="balanced")


score=cross_validate(arbol,X,y,cv=kf,return_train_score=True,return_estimator=True)
print(np.mean(score["train_score"]))
print(np.mean(score["test_score"])) #Muestra un 98% de acierto 
print()

#Al ver los scores podemos decir que realmente no se está sobreajustando el modelo y que es bueno 
print(score["test_score"])

#El estimador con menos score aún así al predecir muestra 1 en todo
"""
mejorModeloIndex = score["test_score"].argmin()
print(mejorModeloIndex)
arbol_aux=score["estimator"][mejorModeloIndex]


arbol_aux.fit(X,y)
y_pred=arbol_aux.predict(X)

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
"""

arbol.fit(X,y)
y_pred=arbol.predict(X)

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

#Guardo el arbol en un archivo
plt.figure(figsize=(12, 8))
plot_tree(arbol,filled=True)
plt.savefig('arbol_decision.png', dpi=300)
plt.close()