arquivo1 = "arquivo_overwrite.txt"

def main():
    #imprime a mensagem
    print('Digite as frases ou digite "sair" para terminar e salvar o arquivo')
    #cria uma lista em branco
    frases = []
    while True:
        entrada = input("> ")
        #se a entrada for igual a sair, quebra o loop while
        if entrada.lower() == "sair":
            break
        #se não for igual a sair, inclua aquela entrada na lista frases
        frases.append(entrada)

    #com o arquivo1 aberto como arquivo
    with open(arquivo1, "w") as arquivo:
        #pra cada frase da minha lista frases
        for frase in frases:
            #salve a frase no arquivo
            arquivo.write(frase + "\n")
    print("Arquivo original criado. Agora vamos formatr o arquivo.")

    #agora vou criar uma lista para receber os dados modificados em modo read
    dadosmodificados = []
    with open(arquivo1, "r") as arquivo:
        #para cada linha no arquivo "arquivo"
        for linha in arquivo:
            #acrescente os dados modificados removendo os espaçamentos e colocando em maiúsculo
            dadosmodificados.append(linha.strip().upper())

    #agora vamos sobrescrever os dados já modificados no arquivo arquivo1
    with open (arquivo1, "w") as arquivo:
        #para cada dado nos dados modificados
        for linha in dadosmodificados:
            #reescreva no arquivo1
            arquivo.write(linha + "\n")
    print("O arquivo foi modificado")

if __name__ == "__main__":
    main()
