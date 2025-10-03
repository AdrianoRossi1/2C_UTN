max_elementos = 10
lista_alumnos = [""] * max_elementos
lista_libros = [0] * 20
lista_comentarios = [""] * max_elementos
cantidad = 0

def agregar_alumno(listas_alumnos, listas_libros, listas_comentarios):
    global cantidad
    if cantidad >= max_elementos:
        print("Ya se alcanzo el maximo de alumnos")
        return cantidad
    while True:
        nombre = input("Ingrese el nombre completo del alumno: ")
        if nombre != "":
            break
        print("Tenes que poner un nombre")
    while True:
        comentario = input("Ingrese un comentario del alumno: ")
        if comentario != "":
            break
        print("Tenes que poner un comentario")
    while True:
        libros = int(input("Ingrese la cantidad de libros: "))
        if 1 <= libros <= 20:
            break
        else:
            print("La cantidad de libros tiene que ser entre 1 y 20")

    listas_alumnos[cantidad] = nombre
    listas_libros[cantidad] = libros
    listas_comentarios[cantidad] = comentario
    cantidad += 1
    print("Alumno agregado correctamente")

    while True:
        seguir = input("Desea agregar otro alumno? (s/n): ").lower()
        if seguir in ("s", "n"):
            break
        else:
            print("Error, responde con s o n")
    if seguir == "s":
        return agregar_alumno(listas_alumnos, listas_libros, listas_comentarios)
    else:
        return cantidad

def mostrar_habitos(listas_alumnos, listas_libros, listas_comentarios, cantidad):
    if cantidad == 0:
        print("No agregaste alumnos")
        return
    print("Lista de alumnos y sus habitos de lectura:")
    for i in range(cantidad):
        print(f"Alumno: {listas_alumnos[i]}, Libros leidos: {listas_libros[i]}, Comentario: {listas_comentarios[i]}")
    promedio = sum(listas_libros[:cantidad]) / cantidad
    print(f"Promedio de libros leidos por alumno: {promedio}")

def ordenar_bubble(listas_alumnos, listas_libros, listas_comentarios, cantidad):
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if listas_libros[j] < listas_libros[j + 1]:
                listas_libros[j], listas_libros[j + 1] = listas_libros[j + 1], listas_libros[j]
                listas_alumnos[j], listas_alumnos[j + 1] = listas_alumnos[j + 1], listas_alumnos[j]
                listas_comentarios[j], listas_comentarios[j + 1] = listas_comentarios[j + 1], listas_comentarios[j]
    print("Lista ordenada por cantidad de libros leidos de manera descendente:")
    for i in range(cantidad):
        print(f"Alumno: {listas_alumnos[i]}, Libros leidos: {listas_libros[i]}, Comentario: {listas_comentarios[i]}")
    mostrar_habitos(listas_alumnos, listas_libros, listas_comentarios, cantidad)

def menu():
    global cantidad
    while True:
        print("Menu:")
        print("1. Agregar alumno")
        print("2. Mostrar habitos de lectura")
        print("3. Ordenar alumnos por cantidad de libros leidos")
        print("4. Salir")
        opcion = int(input("Seleccione una opcion (1-4): "))
        if opcion == 1:
            cantidad = agregar_alumno(lista_alumnos, lista_libros, lista_comentarios)
        elif opcion == 2:
            mostrar_habitos(lista_alumnos, lista_libros, lista_comentarios, cantidad)
        elif opcion == 3:
            ordenar_bubble(lista_alumnos, lista_libros, lista_comentarios, cantidad)
        elif opcion == 4:
            print("Chau, gracias!.")
            break
        else:
            print("Opcion invalida, solo numeros del 1 al 4.")

menu()