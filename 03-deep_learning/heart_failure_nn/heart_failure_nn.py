from keras.api.models import Sequential
from keras.api.layers import Dense,Dropout
from keras.api.utils import to_categorical
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.model_selection import train_test_split


#Cargo el csv
df_clinico=pd.read_csv("historial_clinico.csv",sep=",")

#Muestro la información
print(df_clinico.info())


#for i in df_clinico.columns:
#    print(df_clinico[i].value_counts())
#    print("------------------")


#Borro filas que tengan algún valor nulo
print(df_clinico.isnull().sum())
df_clinico = df_clinico.dropna()

#Transformo estas columnas categóricas
df_clinico = pd.get_dummies(df_clinico, columns=["tension","fumador"])

#Factorizo diabetes y sexo
cod_diabetes = df_clinico['diabetes'].factorize()[1] 
df_clinico['diabetes'] = df_clinico['diabetes'].factorize()[0]

cod_diabetes = df_clinico['sexo'].factorize()[1] 
df_clinico['sexo'] = df_clinico['sexo'].factorize()[0]

df_clinico['anemia'] = df_clinico['anemia'].replace({'no': 0, 'No': 0, 'Si': 1, 'Sí': 1})

#print(df_clinico.T[1])

#Escalo las columnas numéricas
scaler = MinMaxScaler()
columns_to_scale = ["edad", "creatinina_fosfocinasa", "sangre_contraccion","plaquetas","creatinina","sodio","seguimiento"]
df_clinico[columns_to_scale] = scaler.fit_transform(df_clinico[columns_to_scale])

#print(df_clinico.T[1])

X=df_clinico.drop(columns="fallecimiento")

#Categorizo la Y 0-1
df_y=df_clinico["fallecimiento"]
#print(df_y)
y = to_categorical(df_y)

print(X.shape)
print(y.shape)

#Divido los datos y estratifico por y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,shuffle=True, stratify=df_y)

#Creo la red neuronal
modelo = Sequential(name="Clinico")
modelo.add(Dense(30, input_shape = (18,),activation="relu"))
modelo.add(Dropout(0.5))#Aún desactivando el 50% de las neurnas sigue dando un 1 de accuracy
modelo.add(Dense(2,activation="softmax"))
modelo.summary()


modelo.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

#Entreno el modelo con los datos de entrenamiento y vaida los datos de text para calcular el error y la precisión
historico=modelo.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=100,batch_size=1)
#print(historico.history.keys())


#Muestro la gráfica 
plt.xlabel("Epoch")
plt.ylabel("Loss")
# Trazo la precisión en entrenamiento y validación
plt.plot(historico.history["accuracy"], label="accuracy")
plt.plot(historico.history["val_accuracy"], label="val_accuracy")

plt.legend()
plt.show()

# Trazo la pérdida en entrenamiento y validación
plt.plot(historico.history["loss"], label="loss")
plt.plot(historico.history["val_loss"], label="val_loss")

plt.legend()
plt.show()

#Guardo el modelo
modelo.save("modelo_clinico.h5")

