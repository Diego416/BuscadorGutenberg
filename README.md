# BuscadorGutenberg

  # Proceso ETL

    •	La adquisición de los datos se realizó por motivos de rapidez del link “https://github.com/st0263eafit/hadoop-wordcount/raw/master/datasets/gutenberg-txt-es.zip”, el cual corresponde al proyecto Gutenberg.

    •	El Dataset adquirido en el paso anterior fue almacenado en HDFS.

    •	El proceso de transform se realizó al mismo tiempo que se hacía el procesamiento, es decir, dentro de la misma función mapper. En dicho proceso se realizó al limpieza del dataset de caracteres especiales, tildes, números, además se pasaron todas las palabras a minusculas (Este proceso se puede encontrar en el archivo "wc-mrjob.py").
    
    •	Además, luego de realizar el procesamiento se realizó una limpieza del archivo obtenido, dicha limpieza comprende limpieza de comillas("), tabuladores(\t), corchetes([, ]) y espacios en blanco. Esta limpieza se realizó con el fin de dejar el archivo listo para ser utilizado por Skoop (Este proceso se puede encontrar en el archivo "clean.py").

  # Procesamiento

    El procesamiento se realizó mediante el paradigma Map/Reduce con Python, especificamente con la biblioteca MRJob (Este procesamiento se puede encontrar en el archivo "wc-mrjob.py").
    
  # Storage

    El almacenamiento del resultado final se realizó en una base de datos MySql, este almacenamiento se realizó a través de la herramienta Skoop, para realizar el mapeo de HDFS a MySql, la sentencia utilizada fue:
    
      $ sqoop export \
        --connect jdbc:mysql://10.131.137.188:3306/st0263 \
        --username st0263 -P \
        --table jmunozc2WC \
        --export-dir /user/jmunozc2/data_out/out4/clean_data

  # Aplicación

    •	La aplicación se desarrolló en php, además se desplegó en http://10.131.137.239/~jmunozc2/webappbuscador/index.php .Además, esta aplicación se puede encontrar en la carpeta "webappbuscador".

    •	La base de datos utilizada fue MySql, alojada en la máquina 10.131.137.188. Esta base de datos fue poblada por medio de la herramienta Skoop y es accedida desde la App web
