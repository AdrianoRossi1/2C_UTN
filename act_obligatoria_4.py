def ordenar_mayor_a_menor(num1, num2, num3):
    return sorted([num1, num2, num3], reverse=True)

n1= int(input("Ingrese el primer numero: "))
n2= int(input("Ingrese el segundo numero: "))
n3= int(input("Ingrese el tercer numero: "))
print(f"Números ordenados de mayor a menor: {ordenar_mayor_a_menor(n1, n2, n3)}")
