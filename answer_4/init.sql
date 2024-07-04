CREATE TABLE sucursal (
    id_sucursal SERIAL PRIMARY KEY,
    nombre_sucursal TEXT, -- nombre sucursal
    ciudad TEXT, -- ciudad
    pais TEXT, -- país
    jefe_sucursal TEXT -- jefe sucursal
);

CREATE TABLE vendedor (
    id_vendedor SERIAL PRIMARY KEY,
    nombre_vendedor TEXT,
    telefono_vendedor TEXT
);

CREATE TABLE producto (
    id_producto SERIAL PRIMARY KEY,
    nombre_producto TEXT,
    categoria_producto TEXT,
    marca TEXT,
    precio_unitario NUMERIC
);

CREATE TABLE venta (
    id_venta SERIAL PRIMARY KEY,
    id_vendedor INTEGER REFERENCES vendedor (id_vendedor),
    id_sucursal INTEGER REFERENCES sucursal (id_sucursal),
    id_producto INTEGER REFERENCES producto (id_producto),
    unidades_vendidas INTEGER,
    fecha_venta DATE
);

 


INSERT INTO sucursal (nombre_sucursal, ciudad, pais, jefe_sucursal) 
VALUES ('Sucursal Central', 'Santiago', 'Chile', 'Pedro Pérez'),
       ('Sucursal Norte', 'Antofagasta', 'Chile', 'María Rodríguez'),
       ('Sucursal Sur', 'Valdivia', 'Chile', 'Luisa Fernández'),
       ('Sucursal Occidente', 'La Serena', 'Chile', 'Carlos Rodíguez');

INSERT INTO vendedor (nombre_vendedor, telefono_vendedor) 
VALUES ('Juan González', '+56 9 1234 5678'),
       ('Ana López', '+56 9 8765 4321'),
       ('Pedro Pérez', '+56 9 3456 7890'),
       ('Luisa Fernández', '+56 9 6789 0123'),
       ('Carlos Rodíguez', '+56 9 9012 3456'),
       ('Maria Rodríguez', '+56 9 4567 8901'),
       ('Luis Fernández', '+56 9 7890 1234'),
       ('Luisa Rodíguez', '+56 9 0123 4567');

INSERT INTO producto (nombre_producto, categoria_producto, marca, precio_unitario) 
VALUES ('Laptop', 'Electrónicos', 'HP', 1200.50),
       ('Smartphone', 'Electrónicos', 'Samsung', 699.99),
       ('Tablet', 'Electrónicos', 'Apple', 799.99),
       ('Smartwatch', 'Electrónicos', 'Apple', 199.99),
       ('Television', 'Electrónicos', 'LG', 999.99),
       ('Smart TV', 'Electrónicos', 'Samsung', 1499.99),
       ('Camara', 'Electrónicos', 'Canon', 499.99),
       ('Smart Speaker', 'Electrónicos', 'Sony', 299.99),
       ('Audifonos', 'Electrónicos', 'JBL', 99.99);

INSERT INTO venta (id_vendedor, id_sucursal, id_producto, unidades_vendidas, fecha_venta) 
VALUES (1, 1, 1, 1001, '2024-07-01'),
       (2, 2, 2, 2030, '2023-07-02'),
       (3, 3, 3, 15, '2023-07-03'),
       (4, 4, 4, 20, '2023-07-04'),
       (5, 1, 5, 25, '2023-07-05'),
       (6, 2, 6, 30, '2023-07-06'),
       (7, 3, 7, 35, '2023-07-07'),
       (8, 4, 8, 40, '2023-07-08'),
       (1, 1, 9, 45, '2023-07-09'),
       (2, 2, 1, 50, '2023-07-10'),
       (3, 3, 2, 55, '2023-07-11'),
       (4, 4, 3, 60, '2023-07-12'),
       (5, 1, 4, 65, '2023-07-13'),
       (6, 2, 5, 70, '2023-07-14'),
       (7, 3, 6, 75, '2023-07-15'),
       (8, 4, 7, 80, '2023-07-16'),
       (1, 1, 8, 85, '2023-07-17'),
       (2, 2, 9, 10000, '2024-07-18'),
       (3, 3, 1, 95, '2024-07-19');
