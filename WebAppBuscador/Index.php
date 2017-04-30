<html>
 <head>
  <title>Buscador</title>
 </head>
 <style>
    #busqueda{
        position:absolute;
        top:300px;
        left:455px;
        padding: 20px;
        margin-bottom: 1000px;
        text-align: center;
    }
    #text{
        width: 350px;
        height: 30px;
        padding-left:10px;
    }
    #submit{
        width: 100px;
        height: 30px;
    }
 </style>
 <body> 
 
<img id="imgGutenberg" src="img/gutenberg_logo.png" style="position:absolute; top:80px; left:580px" width="200px" height="200px">

 <div id="busqueda">
    <form method="POST" action="result.php">  
        <input id="text" type="text" name="txtBusqueda" autofocus placeholder="Ingrese su busqueda">
        <input id="submit" type="submit" name="submit" value="Buscar">
    </form>
 </div>
 </body>
</html>