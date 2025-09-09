vec_numero = [0] * 10
numero = 0

for numero in range(len(vec_numero)):
    vec_numero[numero] = int(input("Ingrese un numero: ")) 

suma_numeros = 0

for numero in range(len(vec_numero)):
    suma_numeros += vec_numero[numero]
print(f"La suma de los numeros es: {suma_numeros+1}")

