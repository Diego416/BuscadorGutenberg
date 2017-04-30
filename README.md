# BuscadorGutenberg

  # Proceso ETL

    •	La adquisición de los datos se realizó por motivos de rapidez del link “https://github.com/st0263eafit/hadoop-wordcount/raw/master/datasets/gutenberg-txt-es.zip”, el cual corresponde al proyecto Gutenberg.

    •	El Dataset adquirido en el paso anterior fue almacenado en HDFS.

    •	El proceso de transform se realizó al mismo tiempo que se hacía el procesamiento, es decir, dentro de la misma función mapper. En dicho proceso se realizó al limpieza del dataset de caracteres especiales, tildes, números, además se pasaron todas las palabras a minusculas (Este proceso se puede encontrar en el archivo "wc-mrjob.py").

  # Procesamiento

    El procesamiento se realizó mediante el paradigma Map/Reduce con Python, especificamente con la biblioteca MRJob.

  # Aplicación

    •	La aplicación se desarrolló en php, además se desplegó en http://10.131.137.239/~jmunozc2/webappbuscador/index.php

    •	La base de datos utilizada fue MySql, alojada en la máquina 10.131.137.188. Esta base de datos fue poblada por medio de la herramienta Skoop y es accedida desde la App web
