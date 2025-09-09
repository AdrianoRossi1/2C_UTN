
array_1 = []
array_2 = []

print("Ingrese 5 elementos para el primer array:")
for i in range(5):
    valor = input(f"Elemento {i+1}: ")
    array_1.append(valor) 

print("Ingrese 5 elementos para el segundo array:")
for i in range(5):
    valor = input(f"Elemento {i+1}: ")
    array_2.append(valor)

# Comparar arrays
if array_1 == array_2:
    print("Los arrays son iguales.")
else:
    print("Los arrays NO son iguales.")
