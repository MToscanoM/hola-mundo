nombre = input("¿Cómo te llamas? ")
print("Hola ", nombre)

strEdad = input("¿Cuántos años tienes? ")
strAnno = input("¿En qué año estamos? ")
strCumplidos = input("¿Los cumpliste ya este año? ")

edad = int(strEdad)
anno = int(strAnno)

if strCumplidos == "S":
    nacimiento = anno - edad
else:
    nacimiento = anno - edad -1

print(nombre, "naciste en", nacimiento)
