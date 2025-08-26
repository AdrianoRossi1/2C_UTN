def es_par(num):
    return num % 2 == 0 
n= int(input("Ingrese un número: "))
if es_par(n):
    print(f"El número {n} es par.")
else:
    print(f"El número {n} es impar.")