from gestion_parque.parque import registrar_visita, mostrar_resumen, mostrar_atracciones, puede_entrar, calcular_precio

while True:
    nombre = input("Por favor, ingrese su nombre: ")
    if nombre.isalpha():
        break
    else:
        print("Error, el nombre solo debe contener letras.")

while True:
    edad = input("Ingrese su edad: ")
    if edad.isdigit() and int(edad) > 0:
        edad = int(edad)
        break
    else:
        print("Error, la edad debe ser un número.")

mostrar_atracciones()
entrada = 0
atraccion_elegida = ""
contador_montania = 0
contador_terror = 0
contador_carrusel = 0 
contador_atracciones = 0

while True:
    atraccion = int(input("¿A cuál de las siguientes atracciones le gustaría entrar? (1-Montania rusa ; 2-Casa del terror ; 3-Carrusel) "))
    if atraccion not in [1, 2, 3]:
        print("Error, no es una atracción válida.")
        continue
    if not puede_entrar(edad, atraccion):
        if edad < 6:
            print("Lo siento, solo puede ingresar al Carrusel.")
        elif edad <= 12:
            print("Usted solo puede pasar al Carrusel y Casa del Terror.")
        continue
    print("Pase por favor.")
    precio = calcular_precio(atraccion)
    entrada += precio
    if atraccion == 1:
        atraccion_elegida += "Montania rusa "
        contador_montania += 1
        contador_atracciones += 1
    elif atraccion == 2:
        atraccion_elegida += "Casa del terror "
        contador_terror += 1    
        contador_atracciones += 1
    else:         
        atraccion_elegida += "Carrusel "
        contador_carrusel += 1  
        contador_atracciones += 1    
    repetir = input("Espero que lo haya disfrutado!! ¿Le gustaría ir a otra atracción? (si/no) ")
    while repetir not in ["si", "no"]:
        print("Error, opción no válida. Responda con 'si' o 'no'.")
        repetir = input("¿Le gustaría ir a otra atracción? (si/no) ")   
    if repetir == "no":
        break   
if contador_atracciones >= 3:
    print("¡Se aplica un descuento del 10% por subir a 3 o más atracciones!")
    entrada *= 0.90

mostrar_resumen(nombre, edad, contador_montania, contador_terror, contador_carrusel)
print(f"Total a pagar: {entrada}")
if contador_montania == 0:
    print("No subió a la Montaña rusa ")        
if contador_terror == 0:
    print("No entró a la Casa del Terror ")       
if contador_carrusel == 0:
    print("No subió al Carrusel ")







