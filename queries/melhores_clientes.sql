SELECT Nome, Sobrenome, Email, Celular, recency_level, unique_id, COUNT(*) AS Total_Compras
FROM pedidos
WHERE recency_level = 'R5'
GROUP BY unique_id
HAVING COUNT(*) > 2
ORDER BY Total_Compras DESC;