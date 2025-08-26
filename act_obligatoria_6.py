def convertir_minutos_a_horas(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes 
min= int(input("Ingrese la cantidad de minutos: "))
h, m= convertir_minutos_a_horas(min)
print(f"{min} minutos son {h} horas y {m} minutos.")
        