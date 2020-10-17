def esBisiesto(anio):
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
    
num = input("Dame un año: ")
while not num.isdigit():
    num = input("Incorrecto, escribe un número para el año: ")
    
anno = int(num)

if esBisiesto(anno):
    print(anno, "es bisiesto")
else:
    print(anno, "no es bisiesto")