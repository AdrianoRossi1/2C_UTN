def area_triangulo(base, altura):
    return (base * altura) / 2

b= float(input("Ingrese la base del triángulo: "))  
h= float(input("Ingrese la altura del triángulo: "))  
print(f"El área del triángulo es: {area_triangulo(b, h)}")

