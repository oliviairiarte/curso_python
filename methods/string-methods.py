
"""
type(var) te dice el tipo

Transformación de Mayúsculas/Minúsculas ------------------------------------

.upper() / .lower(): Todo a MAYÚSCULAS o minúsculas.
.capitalize(): Primera letra del texto en mayúscula.
.title(): Primera letra de cada palabra en mayúscula.


Limpieza de Espacios -------------------------------------------------------
.strip(): Quita espacios (o caracteres) al inicio y al final.
.lstrip() / .rstrip(): Quita espacios solo a la izquierda o solo a la derecha.

Separación y Unión (Claves para listas)---------------------------------------

.split(): Corta la cadena en una lista (por defecto usa espacios).
.join(): Une una lista en una sola cadena usando un separador.
.splitlines(): Divide el texto donde haya saltos de línea.

Búsqueda y Reemplazo--------------------------------------------------------

.replace("viejo", "nuevo"): Cambia un texto por otro.
.find() / .index(): Devuelve la posición donde empieza una palabra (index da error si no existe).
.count("a"): Cuenta cuántas veces aparece un carácter o palabra.
.startswith("Hi") / .endswith("!"): Devuelve True si empieza o termina con ese texto.

Validación (Devuelven True o False)------------------------------------------

.isalpha(): Solo letras.
.isdigit(): Solo números.
.isalnum(): Solo letras y números.
.isspace(): Solo espacios en blanco.
.islower() / .isupper(): Verifica si todo está en minúsculas o mayúsculas.

Formato y Alineación-----------------------------------------------------------

.zfill(5): Rellena con ceros a la izquierda (ej: 7 -> 00007).
.center(20): Centra el texto en un bloque de X caracteres.
.format(): Inserta variables en llaves {} (aunque ahora se usa más el f-string f"{var}").

"""