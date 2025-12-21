
import pandas as pd

df = pd.read_csv("data2.csv")

# cambiar tipo de dato
df["edad"]= df['edad'].astype(str)
#print(type(df['edad'][0]))

# cambiar un valor
df_nue= df["nombre"].replace('oli','cata')
#print(df_nue)

# borra filas con datos faltantes
#print(df)
df = df.dropna()
print(df)

# filas repetidas
df = df.drop_duplicates()
print(df)

# crear un csv con el df limpio
df.to_csv('files-dalto.py\\datos2_limpios.csv')