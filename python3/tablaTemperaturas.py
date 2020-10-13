def fahrenheitToCentigrados(g):
    return round((g - 32) * 5/9, 2)

def centigradosToFahrenheit(g):
    return g * 9/5 + 32

def centigrados(ini, fin):
    for grados in range(ini, fin+10, 10):
        print("{}ºF -> {}ºC".format(grados, fahrenheitToCentigrados(grados)))

def fahrenheit(ini, fin):
    for grados in range(ini, fin+10, 10):
        print("{}ºC -> {}ºF".format(grados, centigradosToFahrenheit(grados)))
        
tipo = input("Salida (F/C): ")
#tipo = entradaTipo.capitalize()

while tipo.capitalize() != 'C' and tipo.capitalize() != 'F':
    print("Tipo incorrecto")
    tipo = input("Salida (F/C): ")
    
if tipo.capitalize() == 'C':
    centigrados(0,230)
else:
    fahrenheit(0,100)


    