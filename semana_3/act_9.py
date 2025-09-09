numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros[i] = 0

print("Array resultante:", numeros)
