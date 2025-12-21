import re

texto = '''hola genio 1.como andas
hola esta es la linea 2
y esta es la 3'''

#busqueda simple
resul = re.findall('esta',texto)
#print(resul)

# \d --> busca digitos num del 0 al 9 
# \D --> TODO menos dig numericos
# \w --> caract alfanumericos (a-z, A-Z, 0-9, _)
# \s --> busca espacios en blanco y saltos en linea
# \n --> saltos en linea
# . --> todo menos saltos de linea
# \. --> busca los puntos literal 
# / -->cancela car especiales
# ^ --> busca inicio de linea (ver si lo q pensas esta al inicio de linea)
# $ --> final de linea (ejemplo: r'hola$',texto)
# {n} --> n cantidad de veces lo de la izq (r"\d{3},texto) busca 3 dig juntos
# {n,m} --> lo mismo pero en rango (al menos n, max m)

result = re.findall(r"\d", texto)
#print(result)

# buscar patron, EXAMPLE

patron = re.findall(r"\d\.\s", texto)
#print(patron)

buscar = re.findall(r"^hola", texto, flags = re.M) #activa que funcione para cualquier linea
#print(buscar)

# Truco reemplazar patrones

frase = "Hola como estas"
patron = r"^Hola"
nueva = "oculto"

frase_nue = re.sub(patron, nueva, frase)
#print(frase_nue)

# ver si matchea
matchea = re.match(nueva, frase_nue)
if matchea:
    print('si')
else:
    print('no')