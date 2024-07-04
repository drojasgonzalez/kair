DO $$
BEGIN
    RAISE NOTICE '1. Listado de ventas del mes actual (nombre_sucursal, nombre_vendedor, marca, nombre_producto,
fecha_venta, unidades_vendidas, precio_unitario, valor_venta)';
END $$;

SELECT s.nombre_sucursal, 
       v.nombre_vendedor, 
       p.marca, 
       p.nombre_producto, 
       ve.fecha_venta, 
       ve.unidades_vendidas, 
       p.precio_unitario, 
       ve.unidades_vendidas * p.precio_unitario AS valor_venta
FROM venta ve
JOIN sucursal s ON ve.id_sucursal = s.id_sucursal
JOIN vendedor v ON ve.id_vendedor = v.id_vendedor
JOIN producto p ON ve.id_producto = p.id_producto
WHERE EXTRACT(MONTH FROM ve.fecha_venta) = EXTRACT(MONTH FROM CURRENT_DATE)
      AND EXTRACT(YEAR FROM ve.fecha_venta) = EXTRACT(YEAR FROM CURRENT_DATE);


DO $$
BEGIN
    RAISE NOTICE '2. Ventas totales por sucursal, vendedor y marca, incluyendo los vendedores que no tuvieron ventas
(nombre_sucursal, nombre_vendedor, marca, total_venta)';
END $$;

SELECT s.nombre_sucursal, 
       COALESCE(v.nombre_vendedor, 'Sin Vendedor') AS nombre_vendedor, 
       p.marca, 
       COALESCE(SUM(ve.unidades_vendidas * p.precio_unitario), 0) AS total_venta
FROM sucursal s
CROSS JOIN vendedor v
CROSS JOIN producto p
LEFT JOIN venta ve ON ve.id_sucursal = s.id_sucursal 
                AND ve.id_vendedor = v.id_vendedor 
                AND ve.id_producto = p.id_producto
GROUP BY s.nombre_sucursal, v.nombre_vendedor, p.marca
ORDER BY s.nombre_sucursal, v.nombre_vendedor, p.marca;


DO $$
BEGIN
    RAISE NOTICE '3. Productos con más de 1000 unidades vendidas en los últimos 2 meses (nombre_producto, marca,
unidades_vendidas)';
END $$;

SELECT p.nombre_producto, 
       p.marca, 
       SUM(ve.unidades_vendidas) AS unidades_vendidas
FROM producto p
JOIN venta ve ON p.id_producto = ve.id_producto
WHERE ve.fecha_venta >= CURRENT_DATE - INTERVAL '2 months'
GROUP BY p.nombre_producto, p.marca
HAVING SUM(ve.unidades_vendidas) > 1000
ORDER BY unidades_vendidas DESC;


DO $$
BEGIN
    RAISE NOTICE '4. Productos sin ventas en el presente año (nombre_producto, marca)';
END $$;

SELECT p.nombre_producto, 
       p.marca
FROM producto p
LEFT JOIN venta ve ON p.id_producto = ve.id_producto
                  AND EXTRACT(YEAR FROM ve.fecha_venta) = EXTRACT(YEAR FROM CURRENT_DATE)
WHERE ve.id_venta IS NULL
GROUP BY p.nombre_producto, p.marca
ORDER BY p.nombre_producto, p.marca;


DO $$
BEGIN
    RAISE NOTICE '5. De los productos sin ventas en el presente año, monto total de ventas en el año anterior
(nombre_producto, marca, total_venta)';
END $$;

SELECT
    p.id_producto, 
    p.nombre_producto, 
    p.marca, 
    COALESCE(SUM(ve_anterior.unidades_vendidas * p.precio_unitario), 0) AS total_venta
FROM producto p
LEFT JOIN (
    SELECT v.id_producto, 
           SUM(v.unidades_vendidas) AS unidades_vendidas
    FROM venta v
    WHERE EXTRACT(YEAR FROM v.fecha_venta) = EXTRACT(YEAR FROM CURRENT_DATE) - 1
    GROUP BY v.id_producto
) ve_anterior ON p.id_producto = ve_anterior.id_producto
LEFT JOIN venta ve_actual ON p.id_producto = ve_actual.id_producto
                          AND EXTRACT(YEAR FROM ve_actual.fecha_venta) = EXTRACT(YEAR FROM CURRENT_DATE)
WHERE ve_actual.id_venta IS NULL
GROUP BY p.id_producto ,p.nombre_producto, p.marca
ORDER BY p.nombre_producto, p.marca;

