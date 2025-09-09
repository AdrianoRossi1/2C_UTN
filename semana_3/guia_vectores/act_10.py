def buscar_numero(array, numero):
    if numero in array:
        return array.index(numero)
    else:
        return -1

numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]

num_a_buscar = int(input("Ingrese el número a buscar: "))

posicion = buscar_numero(numeros, num_a_buscar)
if posicion != -1:
    print(f"El número se encuentra en la posición {posicion}.")
else:
    print(posicion)

