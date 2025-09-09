vec_numero = [0] * 8
numero = 0
contador_cien = 0

for numero in range(len(vec_numero)):
    vec_numero[numero] = int(input("Ingrese un numero: "))

for numero in range(len(vec_numero)):
    if vec_numero[numero] > 100:
        contador_cien += 1
print(f"La cantidad de numeros mayores a 100 es: {contador_cien}")