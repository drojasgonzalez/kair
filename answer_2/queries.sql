-- PRINT

DO $$
BEGIN
    RAISE NOTICE '1. Seleccione el título y el nombre del autor de todos los libros de la categoría "Ficción".';
END $$;

SELECT titulo, nombre AS autor_nombre
FROM Libros
    JOIN Autores ON Libros.autor_id = Autores.id_autor
WHERE
    categoria_id = 1;

DO $$
BEGIN
    RAISE NOTICE '2. Calcule el precio promedio de todos los libros en la tabla Libros.';
END $$;

SELECT AVG(precio) AS precio_promedio FROM Libros;

DO $$
BEGIN
    RAISE NOTICE '3. Actualice el precio de todos los libros escritos por el autor con id_autor = 5 en un 10% de descuento.';
END $$;

SELECT * FROM Libros where autor_id = 5
UPDATE Libros SET precio = precio * 0.9 WHERE autor_id = 5;

SELECT * FROM Libros where autor_id = 5