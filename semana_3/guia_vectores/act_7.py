vec_numeros = [0] * 6
numeros = 0

for numeros in range(len(vec_numeros)):
    vec_numeros[numeros] = int(input("Ingrese un numero: "))

print(f"Array original: {vec_numeros}")
print("Array invertido:", vec_numeros[::-1])