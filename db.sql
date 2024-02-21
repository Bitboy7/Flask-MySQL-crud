CREATE DATABASE Equipo4;

USE Equipo4;

CREATE TABLE Cafeteria (
    IdPedido INT AUTO_INCREMENT PRIMARY KEY, Nombre varchar(50), Apellido VARCHAR(50), Pedido TEXT, Notas TEXT, Sugerencia TEXT, Hora TIME,
);

CREATE TABLE platillos (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key', fecha_creacion TIMESTAMP COMMENT 'Create Time', 
    nombre VARCHAR(255), 
    descripcion text, 
    precio FLOAT
);

ALTER TABLE Cafeteria ADD COLUMN cantidad INT;
ALTER TABLE Cafeteria ADD COLUMN total FLOAT;
ALTER TABLE platillos ADD COLUMN piezas INT;
ALTER TABLE Cafeteria ADD COLUMN platillo_id INT,
ADD CONSTRAINT fk_pedido_platillo FOREIGN KEY (platillo_id) 
REFERENCES platillos(id);

SELECT * FROM cafeteria;

SELECT * FROM platillos;

INSERT INTO  platillos (nombre, descripcion, precio, piezas) VALUES("Picaditas", "picaditas de masa, pollo/carne/chorizo", 55.0, 3
);