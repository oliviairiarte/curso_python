

# leer una(s) linea(s)

#with open("data.txt", "r") as file:  # lo cierra luego automaticamente
   # content = file.readlines()
   # print(content)

# sobreescribir
with open("data.txt", "w") as file:  # lo cierra luego automaticamente
   # file.write("chauu") 
    file.writelines(["primera linea nue\n", "segunda linea nue"])

