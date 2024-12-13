db.Estudiantes.insertMany([
    { nombre: "Juan Perez", edad: 18, ciudad: "Bogotá" },
    { nombre: "María Gómez", edad: 22, ciudad: "Medellín" },
    { nombre: "Carlos López", edad: 25, ciudad: "Bogotá" },
    { nombre: "Ana Torres", edad: 19, ciudad: "Cali" }
]);

db.Estudiantes.find({});

db.Estudiantes.find({ ciudad: "Bogotá" });

db.Estudiantes.find({ edad: { $gt: 20 } });