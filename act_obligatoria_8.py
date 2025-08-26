def calcular_edad(año_nacimiento):
    año_actual = 2025
    return año_actual - año_nacimiento
año_nac= int(input("Ingrese su año de nacimiento: "))
edad= calcular_edad(año_nac)
print(f"Tenes {edad} años.")  
