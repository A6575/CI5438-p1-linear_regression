### CI5438 - AJ2025
# Proyecto 1

## Regresión Lineal

### Resumen
El objetivo de este proyecto es la familiarización con el algoritmo de regresión lineal,  así como su uso sobre diversos conjuntos de datos. 
Para ello se pide que se implemente dicho algoritmo en el lenguaje imperativo de su preferencia; para luego evaluar esa implementación sobre 3 conjuntos de datos, de diferente complejidad.


### Descripción

#### Parte 1
Implemente el algoritmo de Descenso del Gradiente para resolver una Regresión Lineal Multiple en el lenguaje de programación de su preferencia entre C, C++, Java o Python.


#### Parte 2

Pruebe su implementación del algoritmo con los siguiente conjuntos de datos simples:

  2.1) Peso corporal en función del peso de cerebro (1 rasgo); disponible en http://people.sc.fsu.edu/~jburkardt/datasets/regression/x01.txt [Fecha de Consulta: 21 de Mayo 2025]. 
 
  Para estos datos:
  
    2.1.1) Para estos datos sin normalizar: 

      a) Muestre la curva de convergencia (J() vs. Iteraciones) para alpha = 0,0001.

      b) Realice un scatteplot de los datos junto con la curva que minimiza la función de costo.

      c) Describa brevemente sus resultados

    2.1.2) Para estos datos normalizados (recuerden incluir en su reporte la descripción de la normalización realizada)

      a) Muestre la curva de convergencia (J() vs. Iteraciones) para alpha = 0,0001.
  
      b) Realice un scatteplot de los datos junto con la curva que minimiza la función de costo.

      c) Describa brevemente sus resultados y compárelos con los de los datos sin normalizar. Para realizar esta comparación pueden dibujar ambas 
      curvas sobre la misma gráfica o simplemente comparar los mejores errores obtenidos en cada caso. Pueden incluir en su comparación los tiempos 
      de corrida de ambos entrenamientos (sin normalizar y normalizados).
      
    

  2.2) Tasa de homicidios por millón de habitantes (3 rasgos); disponible en: http://people.sc.fsu.edu/~jburkardt/datasets/regression/x08.txt [Fecha de Consulta: 21 de Mayo 2025].

  
    2.2.1) Para estos datos normalizados y sin normalizar:  Muestre las curvas de convergencia (J() vs. Iteraciones) para alpha = 0.0001. Describa brevemente sus resultados, incluya su respuesta a la pregunta ¿Hace falta normalizar, o simplemente es útil?. 

    2.2.2) Para los datos normalizados muestre las curvas de convergencia (J() vs. Iteraciones) para alpha = 0.0001, 0.001,  0.01, 0.1, 1. Describa brevemente sus
    resultados incluya su respuesta a la pregunta ¿Cómo afecta la tasa de convergencia a los resultados obtenidos?. 


#### Parte 3
Construya tres modelos que incluyan cierta cantidad  de rasgos de datos del conjunto propuesto en el artículo Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project [1]  para predecir el precio de venta (SalePrice) de un bien raíz. Los datos ya no se encuentran en la dirección dada en [1], pero se encuentran disponibles en: https://garthtarr.com/data/AmesHousing.txt;  y las descripción de los mismos está disponible en https://garthtarr.com/data/DataDocumentation.txt [Fecha de Consulta: 21 de Mayo 2025]. 
  

Para esto deberá:

  a) Limpiar los datos, usando las instrucciones de artículo de DeCock [1] (sección 5)
  
  b) Normalizar los datos resultantes de la limpieza. 
  
  c) Escoger el 80% de los datos para entrenamiento, y dejar un 20% para la prueba. Cómo hacen esta separación?  

  d) Tome o escoja los rasgos para cada modelo:
    - Modelo 0: Total Basement y Gr Liv Area. 
    - Modelo 1: Total Basement, Gr Liv Area, LotArea, Garage Cars y FireYN.
    - Modelo 2: Total Basement, Gr Liv Area + 3 atributos a escoger (Deben ser diferentes al Modelo 1). Comenten en el informe cómo seleccionan los atributos adicionales.
    
  e) Evalúe los resultados de cada modelos en sobre los datos de entrenamiento y sobre los de prueba usando las cuatro metricas propuestas en la seccion 4 de [1]. Discuta brevemente sus resultados




### Entrega:

* Deberán subir al repositorio de su tarea un informe con sus respuestas a las actividades, en formato PDF, el archivo debe llevar por nombre "Reporte.pdf". El reporte deberá estar en el formato Wenneker Assignment [2].
    
* Deberan agregar un MY_README.md con la información para ejecutar sus proyectos y la descripción del contenido del repositorio.
  
* Su informe (Reporte.pdf) además de incluir las respuestas a cada una de las actividades planteadas en la descripción debe incluir los siguientes elementos: 
  1. Resumen.
  2. Detalles de implementacion/experimentacion. (Lenguaje usado, detalles del algoritmo, cómo normalizan, etc). 
  3. Presentacion y discusion de los resultados (En base a los elementos requeridos para cada conjunto de datos).
  4. Conclusiones.
  5. Referencias.

* Fecha de entrega: Lunes 2 de Junio, hasta las 11:59 pm.

#### Referencias
[1] De Cock, Dean. Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project. Journal of Statistics Education, Volume 19, Number 3, (2011). [Fecha de consulta: 21 Mayo 2025]. Disponible en: http://ww2.amstat.org/publications/jse/v19n3/decock.pdf 

[2] LaTeX Templates."Wenneker Assignment". disponible en: https://www.latextemplates.com/template/wenneker-assignment (consultado el 29/04/2025).
