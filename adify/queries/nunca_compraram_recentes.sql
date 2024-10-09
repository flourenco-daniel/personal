SELECT
    c.CPF,
    c.Nome,
    c.Sobrenome,
    c.Celular,
    c.Email,
    c.Data_de_Cadastro
FROM
    clientes c
LEFT JOIN
    pedidos p ON p.Nome = c.Nome AND p.Sobrenome = c.Sobrenome AND p.Email = c.Email
WHERE
	c.Data_de_Cadastro >= '2024-01-01'
    AND p.CPF IS NULL;