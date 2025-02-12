arquivo = open("dados_write.txt", "w")

conteudo1 = "Primeira linha"
conteudo2 = "Segunda linha"

primeiralinha = arquivo.write(conteudo1)
segundalinha = arquivo.write(conteudo2)

arquivo2 = open("dados_write_lines.txt", "w")

linhas = ("Primeira linha", "\nSegunda linha")

addlinhas = arquivo2.writelines(linhas)

#ponto interessante. Utilizando o "w" (modo write), o py trunca os arquivos, ou seja,
#ele exclui o conteúdo dos arquivos e add de novo. Portanto, se rodarmos varias vezes, conteúdo do arquivo será sempre o mesmo