#vamos chamar o metodo with open para garantir que o arquivo será fechado no final

with open ("dados_write_lines.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)
    print("Fim do arquivo: ", arquivo.name)