CREATE TABLE Estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    ciudad VARCHAR(50) NOT NULL
);

INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES
('Juan Perez', 18, 'Bogotá'),
('María Gómez', 22, 'Medellín'),
('Carlos López', 25, 'Bogotá'),
('Ana Torres', 19, 'Cali');

SELECT * FROM Estudiantes;

SELECT * FROM Estudiantes WHERE ciudad = 'Bogotá';

SELECT * FROM Estudiantes WHERE edad > 20;