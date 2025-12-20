
def obtener_compañeros(cant):
    compañeros= []
    for i in range(cant):
        nombre = input("Ingrese nombre: ")
        edad = int(input("ingrese edad: "))
        print()
        compañero = (nombre,edad)
        compañeros.append(compañero)

    compañeros.sort(key = lambda x: x[1])  #ordena con el criterio edad
    profe = compañeros[-1][0]
    asistente = compañeros[0][0]

    return profe,asistente

profe,asis= obtener_compañeros(4)
print(f"El profe es {profe} y el asistente {asis}")

