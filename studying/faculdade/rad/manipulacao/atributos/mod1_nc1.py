import os

#definindo o arquivo1 da seguinte forma => abra o dados1 caso existe, modo escrita e com encoding utf-8. Caso não existe, ele criará dados1.txt
arquivo1 = open("dados1.txt", 'w', encoding='utf-8')
#aqui estou pedindo pra ele printar o caminho absoluto de arquivo 1, ou seja C://...
print(os.path.abspath(arquivo1.name))
#aqui, quero que ele escreva olá mundo no arquivo1
arquivo1.write("Olá Mundo!")

#aqui eu estou pedindo pra ele citar o caminho relativo (ou seja, dados1.txt)
print(os.path.relpath(arquivo1.name))
print(arquivo1)
#fecha o arquivo
arquivo1.close()