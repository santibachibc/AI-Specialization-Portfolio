from PIL import Image, ImageOps
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np

model = load_model("modelo_dedos.h5")


for i in range(5):
    img_path = f"./foto{i}.jpg"
    img = Image.open(img_path)
    img = ImageOps.exif_transpose(img)  

   
    img = img.convert("L") 
    img = img.resize((224, 224))


    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=-1) 
    img_array = np.expand_dims(img_array, axis=0)   


    pred = model.predict(img_array)
    predicted_class = np.argmax(pred)


    plt.imshow(img_array[0, :, :, 0], cmap="gray")
    plt.title(f"Predicción: {predicted_class}")
    plt.axis("off")
    plt.show()
