<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Datos recibidos del formulario</title>
    <style>
        /* Estilo general */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f9;
            color: #333;
            text-align: center;
        }

        h1 {
            color: #1dc58d;
            text-align: center;
        }

        h2 {
            color: #000000;
            text-align: center;
        }     

    </style>
</head>

    <body>
        <?php
        // Verifica si se envió el formulario
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Captura los datos del formulario
            $nombre = htmlspecialchars($_POST['nombre']);
            $email = htmlspecialchars($_POST['email']);
            $telefono = htmlspecialchars($_POST['telefono']);
            $password = htmlspecialchars($_POST['password']);
            $fecha_nacimiento = htmlspecialchars($_POST['fecha_nacimiento']);
            $pais = htmlspecialchars($_POST['pais']);
            $mensaje = htmlspecialchars($_POST['mensaje']);

            // Muestra los datos recibidos
            echo "<h1>Datos recibidos del formulario:</h1>";
            echo "<h2>Hecho por Esteban Diaz Vargas:</h2>";
            echo "<p><strong>Nombre:</strong> $nombre</p>";
            echo "<p><strong>Correo Electrónico:</strong> $email</p>";
            echo "<p><strong>Teléfono:</strong> $telefono</p>";
            echo "<p><strong>Contraseña:</strong> (Oculta por seguridad)</p>";
            echo "<p><strong>Fecha de Nacimiento:</strong> $fecha_nacimiento</p>";
            echo "<p><strong>País:</strong> $pais</p>";
            echo "<p><strong>Mensaje:</strong> $mensaje</p>";
        } else {
            // Si se accede directamente al archivo sin enviar el formulario
            echo "<h1>Acceso no autorizado</h1>";
        }
        ?>
    </body>
</html>