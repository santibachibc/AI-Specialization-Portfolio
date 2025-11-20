
-----V1------:

Para estos 3 modelos :
LogisticRegression(LR)
LinearDiscriminantAnalysis(LD)
QuadraticDiscriminantAnalysis(QD)


Se observa que QD puede ser descartado, ya que no ofrece un rendimiento tan competitivo como los otros dos modelos. 
En cuanto a la comparación entre LR y LD, la elección no es tan sencilla. Aunque LD tiene un test_score más alto que LR, 
al considerar métricas adicionales y el objetivo específico que queremos lograr, se podría argumentar que LR es una mejor 
opción en este caso.

Aunque LR presenta un test_score menor que LD, tiene una mayor capacidad para identificar correctamente a los pacientes 
que realmente fallecerán (es decir, tiene más verdaderos positivos en cuanto a fallecidos), mientras que LD tiene un mejor 
desempeño identificando a los pacientes que sobrevivirán, pero a costa de cometer más falsos negativos en cuanto a los fallecimientos.

En situaciones clínicas como esta, donde la prioridad es no pasar por alto los casos de pacientes que podrían fallecer, 
sería preferible optar por LR. Esto se debe a que, aunque LR puede cometer algunos errores al identificar supervivientes, 
es más crítico evitar el riesgo de clasificar erróneamente a un paciente como sobreviviente cuando en realidad va a fallecer.



------V2-----:
He usado SVC y grid_search y puedo concluir que de todos el mejor estimador es SVR con kernel rbf


------V3-----:
El arbol de decisión también es muy buena opción ya que el test_score muestra un 0.98% de acierto e incluso utilizando el estimador con menor 
score sacado del cross_validate no falla ningún resultado








SUCIO
Se observa que de los 3 podemos descartar QD pero a la hora de descartar uno de los dos restantes no es tan sencillo,
es cierto que LD tiene un test_score más alto que LR pero al hacer algunas métricas más y baśandonos en lo que queremos 
conseguir se podría decir que usar LR es mejor en este caso y eso es debido a que aunque LR tenga un test_score menor que LD 
tiene un mayor número de aciertos en cuanto a fallecidos pero un menor número de aciertos en cuanto a Supervivientes y LD es al 
revés tiene un mayor número de aciertos en cuanto a supervivientes pero más fallos en cuanto a fallecidos por lo que en este caso y ámbito sería mejor
decir a un paciente que va a morir y que al final no que decirlea un paciente que va a sobrevivir y al final no