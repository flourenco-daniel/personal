#Receba o numero correspodente a operação
operacao = input("Selecione o número da operação desejada: \n \n 1- Soma \n 2- Subtração \n 3- Multplicação \n 4 - Divisão\n\n")
lista_opcoes = ["1", "2", "3", "4"]
if:
    for opcao in len(lista_opcoes):
        if operacao != opcao:
            print ("Escolha uma opção válida")
        break

else:

    numero1 = float(input("\nDigite o primeiro número:"))
    numero2 = float(input("\nDigite o segundo numero:"))

    def soma():
        soma = numero1 + numero2
        return soma
    resultadosoma = soma()

    def sub():
        soma = numero1 - numero2
        return soma
    resultadosub = sub()

    def mult():
        mult = numero1 * numero2
        return mult
    resultadomult = mult()

    def div():
        div = numero1 // numero2
        return div
    resultadodiv = div()

    def resto():
        resto = numero1 % numero2
        return resto
    resultadoresto = resto()

    if operacao == "1":
        print("\nA soma dos dois números é", resultadosoma)
    elif operacao == "2":
        print("\nA subtação dos dois números é", resultadosub)

    elif operacao == "3":
        print("\nA multiplicação dos dois números é", resultadomult)

    elif operacao == "4":
        if resultadoresto == 0:
            print("\nA divisão dos dois números é", resultadodiv)
        else:
            print("\nA divisão dos dois números é", resultadodiv)
            print("O resto da divisão é", resultadoresto)
