
print("Hello world!")

#TIPOS DE VARIABLES --------------------------------------------------------
age = 25 
a = b = c = 10
price = 9.9
name = "Juan"
message = 'Hello, world!'
is_adult = True
has_discount = False 

# This is a single-line comment
"""
This is a
multi-line comment
"""

# OPERADORES LOGICOS ------------------------------------------------------
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

# CONTROL STRUCTURES ---------------------------------------------

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

# While
counter = 0

while counter < 5:
    print(counter)
    counter += 1

# LOOP CONTROL

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

# DATA STRUCTURES -----------------------------------------------------------

# List --------------------------------------------------------------------
fruits = ["apple", "banana", "orange"]

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

# FUNCTIONS -------------------------------------------------------------------
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
    
