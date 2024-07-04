-- Crear tabla Autores
CREATE TABLE Autores (
    id_autor SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(100) NOT NULL
);

-- Crear tabla Categorias
CREATE TABLE Categorias (
    id_categoria SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Crear tabla Libros
CREATE TABLE Libros (
    id_libro SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor_id INT NOT NULL,
    categoria_id INT NOT NULL,
    precio NUMERIC(10, 2) NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES Autores (id_autor),
    FOREIGN KEY (categoria_id) REFERENCES Categorias (id_categoria)
);

-- Insertar autores
INSERT INTO
    Autores (nombre, nacionalidad)
VALUES ('Martin Loprado', 'Chile'),
    ('Federico Lobo', 'Argentina'),
    ('Malvin Laurs', 'Algeria'),
    ('Jeffrey Alcause', 'Bulgaria'),
    ('Alex Insua', 'Bolivia'),
    ('Roberto Toro', 'Paraguay');

-- Insertar categorías
INSERT INTO
    Categorias (nombre)
VALUES ('Ficción'),
    ('Misterio'),
    ('Infantil');

-- Insertar libros
INSERT INTO
    Libros (
        titulo,
        autor_id,
        categoria_id,
        precio
    )
VALUES ('Libro 1', 5, 1, 20.00),
    ('Libro 2', 2, 1, 25.50),
    ('Libro 3', 3, 2, 18.75),
    ('Libro 4', 1, 3, 15.00),
    ('Libro 5', 2, 3, 20.00),
    ('Libro 6', 3, 3, 22.50),
    ('Libro 7', 1, 1, 17.00);

SELECT * FROM Libros;

SELECT * FROM Categorias;

SELECT * FROM Autores;