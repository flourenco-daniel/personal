def somar_numeros(numero1, numero2):
    return numero1 + numero2

def subtrair_numeros(numero1, numero2):
    return numero1 - numero2

def multiplicar_numeros(numero1, numero2):
    return numero1 * numero2

def dividir_numeros(numero1, numero2):
    resultado_divisao = numero1 / numero2
    resto_divisao = numero1 % numero2
    return resultado_divisao, resto_divisao

def exibir_menu():
    print("\nSelecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

# Lista de opções válidas
opcoes_validas = ["0", "1", "2", "3", "4"]

# Loop principal do programa
while True:
    exibir_menu()
    operacao = input("Digite o número da operação desejada: ")

    if operacao not in opcoes_validas:
        print("Opção inválida! Escolha uma opção válida (0 a 4).")
        continue

    if operacao == "0":
        print("Saindo do programa...")
        break

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        if operacao == "1":
            resultadosoma = somar_numeros(numero1, numero2)
            print("\nA soma dos dois números é", resultadosoma)
        elif operacao == "2":
            resultadosub = subtrair_numeros(numero1, numero2)
            print("\nA subtração dos dois números é", resultadosub)
        elif operacao == "3":
            resultadomult = multiplicar_numeros(numero1, numero2)
            print("\nA multiplicação dos dois números é", resultadomult)
        elif operacao == "4":
            resultadodiv, resultadoresto = dividir_numeros(numero1, numero2)
            if resultadoresto == 0:
                print("\nA divisão dos dois números é", resultadodiv)
            else:
                print("\nA divisão dos dois números é", resultadodiv)
                print("O resto da divisão é", resultadoresto)
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números.")
