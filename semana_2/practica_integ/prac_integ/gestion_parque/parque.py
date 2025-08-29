def mostrar_atracciones():
    print(f"Perfecto, los precios de nuestras atraccionnes son: Montania rusa= 1500, Casa del terror = 1200, Carrusel = 800")

def puede_entrar(edad, atraccion):
    if edad < 6:
        return atraccion == 3       
    elif edad <= 12:
        return atraccion in [2, 3]
    else:
        return True

    
def calcular_precio(atraccion):
    if atraccion == 1:
        return 1500
    elif atraccion == 2:
        return 1200
    elif atraccion == 3:
        return 800
    else:
        return 0


def registrar_visita():
    nombre = input("Por favor, ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    atraccion = int(input("¿A cuál de las siguientes atracciones le gustaría entrar? (1-Montania rusa ; 2-Casa del terror ; 3-Carrusel) "))
    return nombre, edad

def mostrar_resumen(nombre, edad, contador_montania, contador_terror, contador_carrusel):
    print(f"Gracias por su visita {nombre}")
    print(f"Nombre: ",nombre)
    print(f"Edad: ", edad)
    print(f"Cantidad de veces subido al carrusel: ", contador_carrusel)
    print(f"Cantidad de veces que entró a la Casa del Terror: ", contador_terror)
    print(f"Cantidad de veces que subió a la Montaña Rusa: ", contador_montania)


