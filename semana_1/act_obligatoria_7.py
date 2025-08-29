def verificar_acceso_edad(edad):
    if edad >= 18:
        return "Acceso permitido"
    else:
        return "Acceso denegado" 
edad_usuario = int(input("Ingrese su edad: "))
print(verificar_acceso_edad(edad_usuario))
