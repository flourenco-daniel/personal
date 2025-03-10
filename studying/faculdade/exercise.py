
#exercise 1: solving using basics of python
import numpy as np
from scipy import stats

lista1 = [5, 8, 10, 10, 12, 15, 18, 20, 20, 24, 25, 25, 25, 30, 38, 45, 52, 52, 60, 65, 70, 70, 79, 84, 90]
lista = []
for numero in lista1:
    numeros = numero*2
    lista.append(numeros)

media = np.mean(lista)
mediana = np.median(lista)
moda = stats.mode(lista)

#exercise 2:

lista2 = [8522, 12630, 7453, 6005, 5874, 6612, 8439, 7531, 6430, 4986]

media = np.mean(lista2)

#exercise 3:

lista3 = [5, 8, 10, 10, 12, 15, 18, 20, 20, 24, 25, 25, 25, 30, 38, 45, 52, 52, 60, 65, 70, 70, 79, 84, 90]
media = np.mean(lista3)
desvio_padrao = np.std(lista3, ddof=0)
# print("Media: ", media, "Desvio padrão:", desvio_padrao)
# print(media + desvio_padrao, media - desvio_padrao)
print(media - min(lista3), max(lista3) - media)
variancia = np.var(lista3)
print(variancia)