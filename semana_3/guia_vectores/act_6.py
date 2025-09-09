vec_numeros = [0] * 7
numero = 0

for numero in range(len(vec_numeros)):
    vec_numeros[numero] = int(input("Ingrese un numero: "))

max_num = vec_numeros[0]
posicion = 0

for numero in range(len(vec_numeros)):
    if vec_numeros[numero] > max_num:
        max_num = vec_numeros[numero]
        posicion = numero
print(f"El numero mayor es: {max_num} y se encuentra en la posicion {posicion+1}")