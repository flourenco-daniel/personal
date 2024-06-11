SELECT
	unique_id,
    Nome,
    Sobrenome,
	COUNT(Pedido) as TotaldeCompras,
    Celular,
    Email,
    recency_level,
    Status
FROM
	pedidos
GROUP BY
	unique_id
HAVING
	TotaldeCompras = 1
    AND
    recency_level IN ('R1', 'Inactive')
    AND
    Status = "Pago"
ORDER BY
	TotaldeCompras DESC