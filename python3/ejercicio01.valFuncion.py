def validacion(mensaje):
    esValido = False
    while not esValido:
        strNum = input(mensaje)
        if strNum.isdigit():
            num = int(strNum) / 10
            esValido = True
        elif strNum != "" and strNum[0] == "-" and strNum[1:].isdigit():
            num = int(strNum) / 10
            esValido = True
        else:
            print(strNum,"no es un número entero")
            esValido = False
    
    return num

# Entrada de datos
numUno = validacion("Introduce un número: ")
numDos = validacion("Introduce otro número: ")

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

