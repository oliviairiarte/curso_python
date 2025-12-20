
print("Hello world!")

# 1.TIPOS DE VARIABLES --------------------------------------------------------
age = 25 
a = b = c = 10
price = 9.9
name = "Juan"
message = 'Hello, world!'
is_adult = True
has_discount = False 

# FUNCIONES BUILT-IN
numero= round(12.3456,2)
print(numero)

result_all= all([234,"kssksks",[234,456]])  #devuelve si todos son true
print (result_all)                          #para uno ser TRUE --> <> de 0, false y none

# This is a single-line comment
"""
This is a
multi-line comment
"""

# 1.2. OPERADORES LOGICOS ------------------------------------------------------
a = 10
b = 3

suma = a + b             # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.333333333
floor_division = a // b # 3
modulus = a % b         # 1
exponentiation = a ** b # 1000

equal = a == b          # False
not_equal = a != b      # True

# 2. CONTROL STRUCTURES ---------------------------------------------

# If Elif Else
"""
if condition1:
    ....
elif condition2:
    ....
else:
    ....
"""

#For (El bloque 'for' SÍ requiere indentación)
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# For en listas
numeros= [1,2,3,4]
for num in enumerate(numeros): #imprime tuplas, indice + valor
    print(num)

# For en diccios
dicc = {
    "nom": "oli",
    "ape": 222
}
for datos in dicc.items():
    key = datos[0]
    value = datos[1]  #datos es TUPLA

# While
counter = 0

while counter < 5:
    print(counter)
    counter += 1

# 3. LOOP CONTROL

# Break
counter = 0
while True:
    print(counter)
    counter += 1
    if counter == 5:
        break

# Continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)        # el continue esquiva el print y te devuelve a una nueva vuelta

print("-" * 20)

# 4. DATA STRUCTURES -----------------------------------------------------------

# List --------------------------------------------------------------------
fruits = ["apple", "banana", "orange"]
list_v2 = list([3,4,5])


print(fruits[0])  # Prints "apple"
print(fruits[1])  # Prints "banana"
print(fruits[2])  # Prints "orange"

print(fruits[-1])  # Prints "orange"
print(fruits[-2])  # Prints "banana"
print(fruits[-3])  # Prints "apple"

# List methods

fruits.append("pear")
print(fruits)  # Prints ["apple", "banana", "orange", "pear"]

fruits.insert(1, "grape")
print(fruits)  # Prints ["apple", "grape", "banana", "orange", "pear"]

fruits.remove("banana")
print(fruits)  # Prints ["apple", "grape", "orange", "pear"]

removed_fruit = fruits.pop(2)
print(fruits)  # Prints ["apple", "grape", "pear"]
print(removed_fruit)  # Prints "orange"

fruits.sort()
print(fruits)  # Prints ["apple", "grape", "pear"]

fruits.reverse()
print(fruits)  # Prints ["pear", "grape", "apple"]

# List comprehensions

# new_list = [expression for element in sequence if condition]
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers if x % 2 == 0]
print(squares)  # Prints [4, 16]


# Tuple (inmutable and ordered structure) -------------------------------------------
point = (3, 4)
tupla_v2 = tuple((2,3,4))

print(point[0])  # Prints 3
print(point[1])  # Prints 4

# Methods
my_tuple = (1, 2, 3, 2, 4, 2)
print (my_tuple.index(2))   # Output: 1 (element to search)
print (my_tuple.index(2, 2))   #Output: 3 (element .. , begin position)
print (my_tuple.index(2, 2, 4))   #Output: 3 (element.. , begin, end)

print (my_tuple.count(2)) # Output: 3 / Amount of times an element appears 
print (len(my_tuple))  # Output: 6 / Turple length


# Dictionary ----------------------------------------------------------------
# mutable and unordered structure that stores key-value pairs. 

person = {"name": "Juan", "age": 25, "city": "Madrid"}
dict_version2 = dict(nombre="oli", ape=22)

diccio = dict.fromkeys(["nombre", "ape", "edad"])

print(person["name"])  # Prints "Juan"
print(person["age"])    # Prints 25
print(person["city"])  # Prints "Madrid"

# Dictionary methods
print(person.keys())    # Prints dict_keys(["name", "age", "city"])
print(person.values())  # Prints dict_values(["Juan", 25, "Madrid"])
print(person.items())   # Prints dict_items([("name", "Juan"), ("age", 25), ("city", "Madrid")])


person.update({"profession": "Engineer"})
print(person)  # Prints {"name": "Juan", "age": 25, "city": "Madrid", "profession": "Engineer"}

print("-" * 50)

# Set ---------------------------------------------------------------
#fruits = {"apple", "banana", "orange"}

numbers = set([1, 2, 3, 4, 5])
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2
print(union)  # Prints {1, 2, 3, 4, 5}

intersection = set1 & set2
print(intersection)  # Prints {3}

difference = set1 - set2
print(difference)  # Prints {1, 2}

symmetric_difference = set1 ^ set2
print(symmetric_difference)  # Prints {1, 2, 4, 5}

# Set methods
fruits = {"apple", "banana", "orange"}

fruits.add("pear")
print(fruits)  # Prints {"apple", "banana", "orange", "pear"}

fruits.remove("banana")
print(fruits)  # Prints {"apple", "orange", "pear"}

fruits.discard("grape")
print(fruits)  # Prints {"apple", "orange", "pear"} porque no esta uva

fruits.clear()
print(fruits)  # Prints set()
print("-"*40)

# 5. FUNCTIONS -------------------------------------------------------------------
def greeting():
    print("Hello, world!")
greeting()  # Prints "Hello, world!"

def greeting(name):
    print(f"Hello, {name}!")
greeting("John")  # Prints "Hello, John!"

# Return values
def suma_dos(a, b):
    return a + b
result = suma_dos(3, 4)
print(result)  # Prints 7

# Anonymus function (Lambda)
square = lambda x: x ** 2
print(square(5))  # Prints 25

# Example with Lambda function
numeros = [2,3,4,5,6]
pares = filter(lambda numero: numero%2 == 0, numeros)
print(list(pares))
 
 
# Variable scope (alcance)
def function():
    local_variable = 10
    print(local_variable)  # Accessible within the function

global_variable = 20

def function2():
    print(global_variable)  # Accessible from anywhere

function()  # Prints 10
function2()  # Prints 20
print(global_variable)  # Prints 20
# print(local_variable)  Generates an error, the variable is not defined in this scope.

# Example

def promedio(*numeros):
    sumita = sum(numeros)
    cant = len(numeros)
    prom = sumita/cant
    return prom
print("Promedioooo:", promedio(10,20,30,40))

# Example 2

def variable_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(variable_sum(1, 2, 3))  # Prints 6
    
# 6. Exceptions (mistakes)-----------------------------------------------------------------------
"""
try, bloque que se intenta ejecutar y que puede generar un error (excepción).

except, Bloqueque se ejecuta SOLO si ocurre una excepción en el bloque try.

else, se ejecuta SOLO si el bloque try finaliza con éxito (sin lanzar ninguna excepción).

finally, se ejecuta SIEMPRE, sin importar si hubo error o no, tareas de limpieza (cerrar archivos...)

customized.
"""

# Example 

def realizar_operacion():
    # Inicializa variables para evitar NameError en 'finally'
    resultado = None

    try:
        print("--- Bloque TRY: Intentando realizar la operación ---")
        
        dividendo = int(input("Introduce el dividendo (número de arriba): "))
        divisor = int(input("Introduce el divisor (número de abajo): "))
        
        # Código que puede fallar (ZeroDivisionError)
        resultado = dividendo / divisor
        
    except ValueError:
        # 1. Se ejecuta si el usuario introduce texto en lugar de números.
        print("\n!!! EXCEPTION: Tipo de dato inválido. Debes introducir un número entero.")
        
    except ZeroDivisionError:
        # 2. Se ejecuta si el divisor es 0.
        print("\n!!! EXCEPTION: División por cero no permitida.")
        
    except Exception as e:
        # 3. Captura cualquier otro error inesperado.
        print(f"\n!!! EXCEPTION: Ocurrió un error inesperado: {e}")
        
    except IndexError:
        print("Error: Faltan números para realizar la operación.")
        
    else:
        # Se ejecuta SOLO si el TRY tuvo éxito (no hubo errores).
        print("\n--- Bloque ELSE: Éxito en la operación ---")
        print(f"La división de {dividendo} / {divisor} es: {resultado}")
        
    finally:
        # Se ejecuta SIEMPRE, haya o no habido un error.
        print("\n--- Bloque FINALLY: Proceso de limpieza o finalización ---")
        print("La operación ha terminado.")
        print("-" * 30)

realizar_operacion() 
print()

# Customized exception
# Ejemplo DE 'raise'

def verificar_edad(edad):
    if edad < 18:
        # Lanza una excepción personalizada si la regla falla
        raise ValueError("La edad mínima requerida es 18 años.") 
    return "Edad verificada correctamente."

edad_ingresada = 16
try:
    # Se intenta verificar la edad (con riesgo de fallar)
    resultado = verificar_edad(edad_ingresada)
    print(resultado)

except ValueError as e:
    # Captura el error lanzado por 'raise'
    print(f"!!! ERROR DETECTADO: {e}") 

finally:
    print("--- Proceso finalizado. ---")

# 7. INPUTS AND OUTPUTS ----------------------------------------------------------------------
# User data input: The input() function always returns a string

name = input("Enter your name: ")
print("Hello, " + name + "!")

# For integers or floats
age = int(input("Enter your age: "))

# Data output
name = "Juan"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.")

# 7.2. Reading and writing files -------------------------------------------------------------------------------
"""
Modos de apertura de archivos
- r (read): solo podes leer, puntero al inicio
- a (append,anexar): se abre para escribir AL FINAL (a+ deja leer)
- w (write): se borra todo lo q habia y podes escribir desde el inicio
- w+ (write and read): se borra todo, podes escribir al inicio y leer todo
"""

# Read a file
file = open("data.txt", "r") #read mode: r
content = file.read()
print(content)
file.close()

# Writing a file
file = open("data.txt", "w+") # writing mode: w. If it does not exist it´ll create a new one
file.write("Hello, world!")
content2 = file.read()
print(content)
file.close()

with open("data.txt", "r") as file:  # lo cierra luego automaticamente
    content = file.read()
    print(content)

# 8. Importing and creating modules------------------------------------------------------------------------
# Importing Python modules

import math
result = math.sqrt(25)
print(result)  # Prints 5.0

# Functions and classes of standard modules
""" 
- math: provides sqrt, sin, cos
- random: provides random() and randomint(range)
- datetime: provides .now, .time, .date
"""
import random
import datetime

random_number = random.randint(1, 10)
print(random_number)  # Prints a random integer between 1 and 10
current_date = datetime.datetime.now()
print(current_date)  # Prints the current date and time

# 8.1. Creating my modules ---------------------------------------------------------------------------
# I created a new file with my new and own module

import my_module

my_module.greet("Juan")  # Prints "Hello, Juan!"
result = my_module.calculate_sum(5, 3)
print(result)  # Prints 8

# 9. Packages ----------------------------------------------------------------------------------
# organise related modules into a hierarchical structure, avoid name conflicts.

# Create and use packages

from my_package import module1, module2
print("Este numero mas dos es:", module1.function1(2))
print("La suma de estos numeros es: ", module2.function2(3,3))