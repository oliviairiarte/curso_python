
# pasar lista con nombre y lista con apellido a archivo plano
nombres = ["a", "b", "c", "d"]
apes = ["ka", "ke", "ki", "ko"]

with open("informacion.txt", "w") as file:
    file.write("Datos :\n\n")
    [file.writelines(f"Nombre: {n}\nApellido: {a}\n------------\n") for n,a in zip(nombres,apes)]