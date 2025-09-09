vec_decimal = [0.0] * 6
decimal = 0.0
suma_decimales = 0.0

for decimal in range(len(vec_decimal)):
   vec_decimal[decimal] = int(input("Ingrese un decimal: "))

for decimal in range(len(vec_decimal)):
    suma_decimales += vec_decimal[decimal]

promedio_decimales = suma_decimales / len(vec_decimal)
print(f"El promedio de los decimales es: {promedio_decimales}")
   

