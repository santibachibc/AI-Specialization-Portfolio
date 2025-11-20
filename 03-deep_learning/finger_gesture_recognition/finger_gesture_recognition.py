from keras.models import Sequential
from keras.layers import Conv2D, AvgPool2D, Flatten,Dense, Dropout
import matplotlib.pyplot as plt
from keras.utils import image_dataset_from_directory
import numpy as np



#Cargo los datos
datos_train,datos_test=image_dataset_from_directory("./dedos",labels="inferred",label_mode="categorical",class_names=["0","1","2","3","4","5"],color_mode="grayscale",batch_size=10,image_size=(224,224),shuffle=True,seed=7,validation_split=0.3,subset="both",crop_to_aspect_ratio=False)

#Metodo para pasar los datos de tensorflow a numpy
def transformarDatos(datos):
   
    x_list = []
    y_list = []


    for x, y in datos_train:
        x_list.append(x.numpy()) 
        y_list.append(y.numpy())


    X = np.concatenate(x_list, axis=0)
    y = np.concatenate(y_list, axis=0)
    X = X / 255.0
    return X,y

X_train, y_train=transformarDatos(datos_train)
X_test, y_test=transformarDatos(datos_test)

#print(X_test.shape)
#print(y_test[7])

#Creo la red
model=Sequential()

model.add(Conv2D(10,(3,3),activation="relu",input_shape=(224,224,1)))

model.add(Conv2D(6,(4,4),activation="relu"))

model.add(AvgPool2D((2,2)))

model.add(Flatten())

model.add(Dense(2000,activation="relu"))

model.add(Dropout(0.55))

model.add(Dense(400,activation="relu"))

model.add(Dense(6,activation="softmax"))

model.summary()

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

historico=model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=10,batch_size=10)
print(historico.history.keys())


#Muestro las gráficas
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.plot(historico.history["accuracy"], label="accuracy")
plt.plot(historico.history["val_accuracy"], label="val_accuracy")

plt.legend()
plt.show()


plt.plot(historico.history["loss"], label="loss")
plt.plot(historico.history["val_loss"], label="val_loss")

plt.legend()
plt.show()


#Guardo el modelo
model.save("modelo_dedos.h5")
