SELECT
	unique_id,
    COUNT(Pedido) as TotaldeCompras,
    Nome,
    Sobrenome,
    Celular,
    Email,
    recency_level
FROM
	pedidos
GROUP BY
	unique_id
HAVING
	TotaldeCompras > 1
    AND
    recency_level IN ('R1', 'Inactive')
ORDER BY
	TotaldeCompras DESC