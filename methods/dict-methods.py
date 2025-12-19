
diccionario = {
    "nombre": "oli",
    "edad": 54,
    0: 33
}

#1
claves= diccionario.keys()
print(claves)

#2
print(diccionario.get("kk"))  #busca el value de esa key. SI NO ESTA DA NONE
print(diccionario[0]) #LANZA ERROR SI NO EXISTE POS

#3
diccionario.pop("nombre")
print(diccionario)

#4
dicc_iterable = diccionario.items()
print(dicc_iterable)

#5
diccionario.clear() #lo limpia todo