vec_numeros = [0] * 10
numero = 0

for numero in range(len(vec_numeros)):
    vec_numeros[numero] = int(input("Ingrese un numero: "))

buscar = int(input("Ingresa un numero entero a buscar: "))
encontrado = False
for numero in vec_numeros:
    if numero == buscar:
        encontrado = True
        print(f"El numero {buscar} se encuentra en la lista")
        break
if not encontrado:
    print("El numero no se encuentra en la lista")
