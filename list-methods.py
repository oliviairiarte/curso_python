

# - list: crea una lista
lista = list(["hola", 2, 34])

# - len: cuenta cant de elementos de una lista
aux = len(lista)

# - append: agrega elem al final
lista.append("chau")

# - insert: agrega a la lista en el indice especificado
lista.insert(2,"kaka")
print(lista)

# - extend: agregar varios elem a la lista
lista.extend([222, "lolo"])


# - pop: elimina elemento, pide indice y devuelve valor
lista.pop(0)

# - remove: remueve un elem, pide valor
lista.remove(222)

# - clear: elimina todos los elem
lista.clear()

# - sort: ordena lista de ascendente a descendente
# SOLO CON BOOLEANOS Y NUMEROS
lista.sort()

# - reverse: invierte todos los elem
lista.reverse() #incluso con cualquier dato

