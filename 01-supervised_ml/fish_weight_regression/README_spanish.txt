Notas de versiones:

V1
Al principio probé qué modelo era mejor utilizando K-Fold y cross_validate. Como no sabía que podía 
obtener el modelo directamente de cross_validate, volví a entrenarlo con PolynomialFeatures, dividiendo 
los datos manualmente para realizar predicciones.

V2
Descubrí que, usando return_estimator=True, podía devolver los estimadores y seleccionar el mejor para 
predecir, evitando la necesidad de entrenar de nuevo.

V3
Aprendí que era mejor utilizar StratifiedKFold para dividir los datos proporcionalmente. Sin embargo, 
dividí los datos manualmente porque no sabía cómo usar StratifiedKFold con cross_validate cuando quería 
estratificar por un valor de X en lugar de Y.

V4
Esta versión es similar a V3, pero en lugar de quedarme con el modelo con mejor puntuación, entreno 
nuevamente el modelo con todos los datos X e Y. Esto permite obtener un modelo más preciso que en V3, 
ya que utilizo todo el conjunto de datos.

V5
En esta versión aprendí a usar StratifiedKFold junto con cross_validate, lo que reduce considerablemente 
la cantidad de código. Verifiqué que, utilizando la misma semilla para dividir los datos en V4 y V5, se 
obtiene la misma puntuación, confirmando que ambos enfoques son equivalentes.

V6
Aquí utilicé GridSearchCV con el estimador SVR para encontrar los mejores parámetros. Luego comprobé las 
puntuaciones de entrenamiento y prueba para evaluar si el kernel seleccionado era adecuado. Si los parámetros 
eran buenos, se podía intuir un buen rendimiento. Finalmente, creé un modelo con los mejores parámetros y lo 
entrené con todos los datos X e Y.













































--Lienzo Sucio--


------V1-------
Al principio probe que modelo era mejor con un Kfold y un cross_validate y como no sabía que 
podía coger el modelo directamende de cross_validate volví a entrenar con polynomial y 
dividiendo los datos manualmente para poder predecir
------V2-------
Aquí aprendí que podía con return_estimator=True devolver los estimadores y coger el mejor 
para predecir y no me hacia falta entrenar de nuevo
------V3-------
En esta versión aprendí que mejor era usar StratifiedKFold para dividir proporcionalmente y 
dividí los datos a mano ya que no sabía como usar el StratifiedKFold con cross_validate cuando no quería 
estratificar por Y sino por un valor de X
------V4-------
Aquí lo que cambia es que es igual que V3 pero al final el modelo que me quedo no es el de mejor score 
como hago en V3 sino que al saber que el estimador que uso es bueno, al final entreno el modelo con todo 
X e Y para que el modelo sea más preciso que en el V3
------V5-------
En el V5 aprendí ha usar el StratifiedKFold junto con cross_validate y funciona igual que V4 pero con mucho menos 
código, comprobando que si uso un semilla para dividir los datos en V4 y V5 da el mismo score por lo que es lo mismo
------V6-------
Aquí uso el estimador SVR uno GridSearchCV para averiguar cuales son los mejores parámetros para SVR luego veo el 
test y train score para saber si es un buen kernel aunque si el score para los parámetros ya es bueno se puede intuir, 
y luego creo un modelo con los mejores parámetros y lo entreno con todos los X e Y