lista = []

for i in range (5):
    a = int(input(f"Coloque o número {i+1}:"))
    lista.append(a)

for indice,numero in enumerate(lista):
    print(f"Número {numero} está na posição {indice}")