# Entrada de datos
# Validación primer número
esValido = False
while not esValido:
    strNumUno = input("Introduzca un número: ")
    if strNumUno.isdigit():
        numUno = int(strNumUno) / 10
        esValido = True
    elif strNumUno[0] == "-" and strNumUno[1:].isdigit():
        numUno = int(strNumUno) / 10
        esValido = True
    else:
        print("No has escrito un número entero")
        esValido = False
# Validacion segundo número        
esValido = False
while not esValido:
    strNumDos = input("Introduzca otro número: ")
    if strNumDos.isdigit():
        numDos = int(strNumDos) / 10
        esValido = True
    elif strNumDos[0] == "-" and strNumDos[1:].isdigit():
        numDos = int(strNumDos) / 10
        esValido = True
    else:
        print("No has escrito un número entero")
        esValido = False        

# Procesamiento de datos
suma = round(numUno + numDos,1)
resta = round(numUno - numDos,1)
multip = round(numUno * numDos,2)
division = round(numUno / numDos,2)

# Salida de resultados
print(numUno," + ",numDos," = ",suma)
print(numUno," - ",numDos," = ",resta)
print(numUno," · ",numDos," = ",multip)
print(numUno," / ",numDos," = ",division)
