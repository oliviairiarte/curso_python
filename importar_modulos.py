
#importar

import my_module as caca # le pongo alias simple

# DOS CASOS ----------------------

# 1. si tengo carpeta A con una carpeta B con modulo SALUDAR, y ESTOY EN CARPETA A
""" 
import carpetaB.saludar as pepito
carpetaB.saludar.saludar --> saludar es LA FUNCION EN EL MODULO 
"""

# 2. tengo carpeta A con carpeta B con modulo SALUDAR (esta atras mio), y ESTOY EN CARPETA C
# ENRUTAMIENTO DE MODULOS

import sys #modulo built in

print(sys.path)
sys.path.append("c:\\Users\\User\\Desktop\\Python 2025-2026\\Curso\\my_package")

import module2 as hola

print(hola.function2(2,3,4,5))

