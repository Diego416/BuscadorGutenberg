<?php
// Start the session
session_start();

// Create connection
$conn = new mysqli("10.131.137.188", "st0263", "st0263.2017", "st0263", "3306");
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Desactivar toda notificación de error
error_reporting(0);
 
// Notificar solamente errores de ejecución
error_reporting(E_ERROR | E_WARNING | E_PARSE);
?>

<?php
    $sql = "Select * from jmunozc2WC where Word='".$_POST['txtBusqueda']."'";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            // output data of each row
            echo "<table>";
            while($row = $result->fetch_assoc()) {
                echo "Se obtuvieron <b>" . $row["WordId"] . "</b> resultados para la palabra <b>" . $row["Word"] . "</b>";
            }
            echo "</table>";
        } else {
            echo "0 results";
        }
        $busqueda = $_POST["txtBusqueda"];
 ?>