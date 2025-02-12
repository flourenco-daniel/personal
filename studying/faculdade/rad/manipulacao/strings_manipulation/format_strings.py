#Olá, {}. Você tem {} anos.".format("João", 25) -- As chaves serão substituidas pelos argumentos da função
#exemplo

def exemplo1():
    nome = "Maria"
    idade = 30
    mensagem = "Olá, {}. Você tem {} anos.".format(nome, idade)
    print(mensagem)

def exemplo2():
    nome = "Carlos"
    idade = 28
    mensagem = f"Olá, {nome}. Você tem {idade} anos."
    print(mensagem)


#Precisão numérica (float number)

#metodo format 
def format_floatnumber():
    valor = 3.14159
    print("Pi com 2 casas decimais: {:.2f}".format(valor))
    
#metodo fstring 
def fstring_floatnumber():
    valor = 3.14159
    print(f"Pi com 2 casas decimais: {valor:.2f}")

#Datetime
#metodo format
from datetime import datetime
def format_datetime():
    hoje = datetime.now()
    data_formatada = hoje.strftime("Data: %d/%m/%Y")
    print(data_formatada)

def fstring_datetime():
    hoje = datetime.now()
    data_formatada = f"Data: {hoje:%d/%m/%Y}"
    print (data_formatada)

fstring_datetime()
