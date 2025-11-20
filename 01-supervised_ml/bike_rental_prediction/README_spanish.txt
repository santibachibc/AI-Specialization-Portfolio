-------------V1-----------------

En un primer momento a la hora de borrar columnas pensé en borrar 
instant, ya que no servía para nada. Luego también pensé en borrar,
atemp, ya que parecía redundante al correlacionarse bastante con temp. 
También pensé en borrar hum, incluso la columna mnth, ya que también estaba 
correlacionado con las estaciones del año. Por último también me pareció 
que el año era algo que daba igual pero al cabo de pruebas de borrar y no borrar 
columnas y score de solo 0.5 de test me dí cuenta que el año era algo muy importante 
ya que si contaba el número de bicicletas por año, en 2012 era prácticamente el doble 
de bicis alquiladas que en 2011, por lo que si quitaba el año, era un dato importante a 
tener en cuenta para el modelo. Esto significa que este modelo es complicado que prediga 
las bicicletas de otro año que no sea 2011 o 2012 ya que necesitamos alguna característica 
que no tenemos en el csv como por el ejemplo podría ser el número total de altas en el servicio, 
así si tuvieramos el número de altas de un año cualquiera creo que podría predecir otros años sin problema.

Después de todo esto la V1 solo elimina la columna instant y muestra el score de los diferentes modelos.

-------------V2-----------------
En esta segunda versión una vez supe la importancia de la colummna año implementé la hipótesis que tenía antes sobre borrar las 
columnas redundantes y puedo decir que era buena ya que hay varias columnas que no necesito, incluso consigo un mejor score.
