def registrar_visita():
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    return nombre, edad

def mostrar_atracciones():
    print("Perfecto, los precios de nuestras atracciones son:")
    print("1. Montaña rusa = $1500")
    print("2. Casa del terror = $1200")
    print("3. Carrusel = $800")

def puede_entrar(edad, atraccion):
    if edad < 6:
        return atraccion == 3
    elif edad <= 12:
        return atraccion == 2 or atraccion == 3
    else:
        return atraccion == 1 or atraccion == 2 or atraccion == 3

def calcular_precio(atraccion):
    if atraccion == 1:
        return 1500
    elif atraccion == 2:
        return 1200
    elif atraccion == 3:
        return 800
    return 0

def mostrar_resumen(entrada, nombre, edad, contador_montania, contador_terror, contador_carrusel, atraccion_elegida):
    print("Resumen de visita:")
    print("Gracias por su visita,", nombre)
    print("Edad:", edad)
    print("Atracciones elegidas:", atraccion_elegida)
    print("Total gastado: $", entrada)
    print("Cantidad de veces subido al Carrusel:", contador_carrusel)
    print("Cantidad de veces que entró a la Casa del Terror:", contador_terror)
    print("Cantidad de veces que subió a la Montaña Rusa:", contador_montania)

def main():
    entrada = 0
    atraccion_elegida = ""
    contador_montania = 0
    contador_terror = 0
    contador_carrusel = 0 
    contador_atracciones = 0

    nombre, edad = registrar_visita()
    mostrar_atracciones()

    while True:
        atraccion = int(input("¿A cuál de las atracciones le gustaría entrar? (1-Montania rusa ; 2-Casa del terror ; 3-Carrusel) "))
        
        if atraccion != 1 and atraccion != 2 and atraccion != 3:
            print("Error, no es una atracción válida.")
            continue

        if not puede_entrar(edad, atraccion):
            if edad < 6:
                print("Lo siento, solo puede ingresar al Carrusel.")
            elif edad <= 12:
                print("Usted solo puede pasar al Carrusel y Casa del Terror.")
            continue

        print("¡Pase por favor!")
        precio = calcular_precio(atraccion)
        entrada += precio

        if atraccion == 1:
            atraccion_elegida += "Montania rusa, "
            contador_montania += 1
        elif atraccion == 2:
            atraccion_elegida += "Casa del terror, "
            contador_terror += 1    
        elif atraccion == 3:         
            atraccion_elegida += "Carrusel, "
            contador_carrusel += 1  

        contador_atracciones += 1
        while True:
            repetir = input("¿Le gustaría ir a otra atracción? (si/no): ")
            if repetir == "si" or repetir == "no":
                break
            print("Error, opción no válida. Responda con 'si' o 'no'.")

        if repetir == "no":
            break   

    if contador_atracciones >= 3:
        print("¡Se aplica un descuento del 10% por subir a 3 o más atracciones!")
        entrada *= 0.90
    mostrar_resumen(entrada, nombre, edad, contador_montania, contador_terror, contador_carrusel, atraccion_elegida)

if __name__ == "__main__":
    main()
