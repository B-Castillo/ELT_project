
# UFC-Influencia de habilidades en combate


Uno de los objetivos de este proyecto es saber cuáles son las habilidades de combates más efectivas en el ámbito profesional de las artes marciales mixtas. También poder hacer predicciones en base a esas habilidades con el conjunto de datos que se han extraido, limpiado e insertado en una BD. Esta idea surge por el afán de elaborar una teoría respaldada por datos que pruebe qué método de combate y qué habilidades son más efectivos para este deporte.
 Pero el principal objetivo de este proyecto es probar mis habilidades y los conociminetos adquiridos poniéndolos en práctica en un pequeño proyecto de análisis.
Este trabajo esta abierto a modificarse con el fin de poder mejorar la fiabilidad de los datos y a la mejora de mis habilidades.





# [Extracción](notebooks/Extracci%C3%B3n.ipynb)
---
![](images/espia.png)


En este notebook lo que se pretende es extraer datos utilizando web scrapping. Para ello hemos seguido los siguientes pasos: primero he utilizado un data frame base de una página web en el qeu hay una columna con un conjunto de urls, las cuales hemos utilizado para dirigirme a sus respectivas páginas. En ellas utilicé una función para recopilar los datos utilizando la librería de Selenium. Pora finalizar, guardé estos datos en archivo `.csv`.


# [Limpieza](notebooks/Limpieza.ipynb)
---
![](images/escoba.png)

El principal objetivo de este notebook es conseguir un data frame cuyos datos puedan ser utilizados para un correcto análisis.
Para ello se realizaron los siguientes pasos:
- Se importa el `.csv` y se convierte en data frame para poder trabajar con él.
- Se extrae de cada celda la lista del conjunto de datos que pertenecen a un combate y se asignan a filas diferentes.
- Al no tener longitudes iguales, se necesita corroborar la longitud de los datos de las estadísticas antes de dividir a los peleadores.
- Se dividen los elementos de la lista, ya que pertenecen a diferentes peleadores y se asignan a filas diferentes.
- Se seccionan las estadísticas de las técnicas conectadas y de las intentadas en columnas diferentes.
- Se reasignan los nombres a las columnas y su posición.
- Para finalizar, se guarda el data frame como `.csv`.


# [Carga en BD](notebooks/Carga%20en%20BBDD.ipynb)
---
![](images/BBDD.jpg)

Teniendo ya un archivo `.csv` limpio, se puede proceder a la estructuración, creación e inserción de los datos.
Para ello se han seguido los siguientes pasos:
- Interpretación del universo del discurso sobre el que queremos hacer la BD. En este caso se trata de las relaciones en los combates.
- Creación del modelo conceptual y el esquema E/R.
- Adaptación a las restricciones del modelo lógico y transformación al modelo relacional.
- Creación de la BD en SQL teniendo en cuenta las restricciones semánticas y utilizando como base el esquema relacional.
- Por último: introducción de los datos del `.csv` a SQL a través de Python.

- [BD](BD/UFC_BD.sql) Este es el documento `.sql` con los constructores de cómo está creada la base de datos.


# [Visualización](notebooks/Visualizaci%C3%B3n.ipynb)
---
![](images/grafico.jpg)

El objetivo de la visualización es facilitar la interpretación de los datos recabados e insertados en una BD en la fase anterior.
- Se hace una query para extraer los datos de SQL y convertirlo en un df.
- Con el df se crea una gráfica con la cual se pueden interpretar mejor cuáles son las divisiones más competitivas.
- Después de concluir cuál es la división con mayor competitividad, se utilizó esa división para hacer la siguiente query y su conversión en df.
- Teniendo este último df, se podrá utilizar para la visualización de diversas gráficas para poder sacar una conclusión sobre los posibles combates de los peleadores y sus posibles resultado en la división, que anteriormente se catalogó como la más competitiva.

# [src](src/)
---
Aquí se explicará brevemente la utilidad de cada archivo `.py`.


[**Harvest**](src/harvest.py)
En este archivo se encuentra una función para scrapear utilizada en el notebook de extracción.

[**Soporte**](src/soporte.py)
Este es un `.py` que contiene un conjunto de funciones utilizadas para la limpieza de los datos en el notebook de limpieza.

[**Gráficas**](src/graficas.py)
En este documento se encuentran las funciones necesarias para la conexión con la BD y la cración de gráficas para el notebook de visualización.


# Librerias
---

[import matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)

[import sqlalchemy](https://docs.sqlalchemy.org/en/14/core/tutorial.html)

[from getpass import getpass](https://docs.python.org/3/library/getpass.html)

[import seaborn](https://seaborn.pydata.org/tutorial/introduction)

[import numpy](https://numpy.org/doc/stable/user/absolute_beginners.html)

[from selenium import webdriver](https://selenium-python.readthedocs.io/getting-started.html)

[from webdriver_manager.chrome ](https://automation-remarks.com/2022/python-webdriver-manager/index.html)

[from geopy.geocoders import Nominatim](https://geopy.readthedocs.io/en/stable/)

[from skimage import io](https://scikit-image.org/docs/stable/api/skimage.io.html)
