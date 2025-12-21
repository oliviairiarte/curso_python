
import pandas as pd

df = pd.read_csv("data2.csv")
df_2= pd.read_csv("data2.csv")
#print(df)  # DATA FRAME (bidimensional, no literal archivo)

nombres= df["nombre"]

# SLICING
cadena = "0123456789"
#print(cadena[0:2])

# ordenar Data Frame 
df_ordenado = df.sort_values("edad")
#print(df_ordenado)

df_orde = df.sort_values("ape",ascending= False)
#print(df_orde)

# concatenar dos DFs
nue = pd.concat([df,df_2])
#print(nue)

primeras = df.head(2) #primeras 3
print(primeras)
print()

ultimas = df.tail(1)
print(ultimas)

filas_y_col = df.shape
print(filas_y_col)

#acceder a un valor especifico
print(df.loc[2,"edad"])
print(df.iloc[2,2])
print()

apellidos = df.iloc[:,1] # toda columna 1

mayor_a_30 = df.loc[df["edad"]>19,:]
print(mayor_a_30)