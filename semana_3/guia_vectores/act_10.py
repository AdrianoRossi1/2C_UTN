def buscar_numero(array, numero):
    for i in range(len(array)): 
        if array[i] == numero:   
            return i+1           
    return -1                  

numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]

num_a_buscar = int(input("Ingrese el número a buscar: "))

posicion = buscar_numero(numeros, num_a_buscar)
print(posicion) 
