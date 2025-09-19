max_libros = 20
titulos = [""] * max_libros
ejemplares = [0] * max_libros

def cargar_titulos(titulos, ejemplares, cantidad_libros):
    print("Cargar títulos y ejemplares")
    while cantidad_libros < max_libros:
        titulo = input("Ingrese título (ENTER para cortar): ")
        if titulo == "":
            break
        copias = int(input("Ingrese cantidad de ejemplares: "))

        titulos[cantidad_libros] = titulo
        ejemplares[cantidad_libros] = copias
        cantidad_libros += 1
        print("Libro agregado correctamente.")

    if cantidad_libros == max_libros:
        print("Catálogo completo. No se pueden agregar más títulos.")

    return cantidad_libros


def mostrar_catalogo(titulos, ejemplares, cantidad_libros):
    print("Catálogo completo")
    for i in range(cantidad_libros):
        print(f"{titulos[i]} -> {ejemplares[i]} copias")


def consultar_disponibilidad(titulos, ejemplares, cantidad_libros):
    print("Consultar disponibilidad")
    titulo = input("Ingrese el título: ")
    for i in range(cantidad_libros):
        if titulos[i] == titulo:
            print(f"{titulos[i]} tiene {ejemplares[i]} copias disponibles.")
            return
    print("El título no se encuentra en el catálogo.")


def listar_agotados(titulos, ejemplares, cantidad_libros):
    print("Libros agotados")
    encontrados = False
    for i in range(cantidad_libros):
        if ejemplares[i] == 0:
            print(f"{titulos[i]} -> SIN copias")
            encontrados = True
    if not encontrados:
        print("No hay libros agotados.")


def agregar_nuevo(titulos, ejemplares, cantidad_libros):
    print("Agregar nuevo título")
    if cantidad_libros >= max_libros:
        print("No se pueden agregar más libros. Catálogo lleno.")
        return cantidad_libros

    titulo = input("Ingrese nuevo título: ")
    copias = int(input("Ingrese cantidad de ejemplares: "))

    titulos[cantidad_libros] = titulo
    ejemplares[cantidad_libros] = copias
    cantidad_libros += 1
    print("Libro agregado correctamente.")

    return cantidad_libros


def actualizar_ejemplares(titulos, ejemplares, cantidad_libros):
    print("Actualizar ejemplares (préstamo / devolución)")
    titulo = input("Ingrese el título: ")
    for i in range(cantidad_libros):
        if titulos[i] == titulo:
            print(f"Ejemplares actuales: {ejemplares[i]}")
            cambio = int(input("Ingrese cantidad (+ para devolución, - para préstamo): "))
            ejemplares[i] += cambio
            if ejemplares[i] < 0:
                ejemplares[i] = 0
            print(f"Actualizado: {titulos[i]} -> {ejemplares[i]} copias")
            return
    print("El título no se encuentra en el catálogo.")

def menu():
    cantidad_libros = 0 

    while True:
        print("Menu principal")
        print("1. Cargar títulos y ejemplares")
        print("2. Mostrar catálogo completo")
        print("3. Consultar disponibilidad")
        print("4. Listar títulos agotados")
        print("5. Agregar un nuevo título")
        print("6. Actualizar ejemplares (préstamo / devolución)")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cantidad_libros = cargar_titulos(titulos, ejemplares, cantidad_libros)
        elif opcion == "2":
            mostrar_catalogo(titulos, ejemplares, cantidad_libros)
        elif opcion == "3":
            consultar_disponibilidad(titulos, ejemplares, cantidad_libros)
        elif opcion == "4":
            listar_agotados(titulos, ejemplares, cantidad_libros)
        elif opcion == "5":
            cantidad_libros = agregar_nuevo(titulos, ejemplares, cantidad_libros)
        elif opcion == "6":
            actualizar_ejemplares(titulos, ejemplares, cantidad_libros)
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

menu()