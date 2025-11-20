from keras.applications.vgg16 import VGG16
from keras.models import Sequential
from keras.layers import Dense, Flatten, Rescaling
import matplotlib.pyplot as plt
from tensorflow.keras.utils import image_dataset_from_directory


#Cargo Las fotos
datos_train,datos_val=image_dataset_from_directory("./fotos",labels="inferred",label_mode="categorical",class_names=["Montana","Playa"],color_mode="rgb",batch_size=8,image_size=(224,224),shuffle=True,seed=7,validation_split=0.3,subset="both",crop_to_aspect_ratio=False)


#El método que he utilizado es Feature extraction, usar una red previamente entrenada y ajustar el clasificador a mi modeloa mi modelo. He usado la red VGG16 entrenada con imagenet ya que tiene clases que se relacionan con playa y montaña y así podré conseguir un buen score.
modelo=Sequential()
vgg16 = VGG16(include_top=None , weights="imagenet", input_shape=(224,224,3))
for capa in vgg16.layers:
    capa.trainable = False
modelo.add(Rescaling(1./255.,input_shape=(224,224,3)))
modelo.add(vgg16)
modelo.add(Flatten())  
modelo.add(Dense(224, activation="relu"))
modelo.add(Dense(2, activation="softmax"))

modelo.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
modelo.summary()

historico=modelo.fit(datos_train,validation_data=datos_val,epochs=10)
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

#El resultado es un score del 83,3%