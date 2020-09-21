diasMes = (31,28,31,30,31,30,31,31,30,31,30)

nombre = input("¿Cómo te llamas? ")
print("Hola ", nombre)

strEdad = input("¿Cuántos años tienes? ")
strAnno = input("¿En qué año estamos? ")
strMes = input("¿En qué mes estamos? ")
strDia = input("¿En qué día estamos? ")

edad = int(strEdad)
anno = int(strAnno)
mes = int(strMes)
dia = int(strDia)

transcurridos = 0
indice = 0

while indice < mes - 1:
    transcurridos = transcurridos + diasMes[indice]
    indice = indice + 1
    
transcurridos = transcurridos + dia

prob = transcurridos / 365 * 100
nacimiento = anno - edad

print(nombre, "naciste en", nacimiento, "con una probabilidad de", prob)
print(" o en ", nacimiento - 1, "con una probabilidad de", 100 - prob)
