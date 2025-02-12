import os

dados = "dados1.txt"
arquivo = open(dados, 'r', encoding='utf-8')

print("Nome do arquivo> ", arquivo.name)
print("Modo do arquivo> ", arquivo.mode)

if arquivo.closed == False:
    print("O arquivo está aberto.")
else:
    print("O arquivo está fechado.")

conteudo = arquivo.read()
print("O conteúdo do arquivo é:\n", repr(conteudo))

arquivo.close()

if arquivo.closed == False:
    print("O arquivo ainda está aberto.")
else:
    print("Agora o arquivo está fechado.")

relpath = os.path.relpath(dados)
abspath = os.path.abspath(dados)

print("O arquivo relativo do arquivo é:", relpath)
print("O arquivo absoluto do arquivo é:", abspath)