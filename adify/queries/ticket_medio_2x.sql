SELECT
	unique_id,
    Data_do_pedido,
    CPF,
    CNPJ,
	Nome,
    Sobrenome,
    Celular,
    Email,
	COUNT(unique_id) AS qtde_pedidos,
    AVG(Valor_Total) AS Ticket_medio
FROM
	pedidos
GROUP BY
	unique_id
HAVING
	qtde_pedidos > 1
ORDER BY
	Ticket_medio
    DESC