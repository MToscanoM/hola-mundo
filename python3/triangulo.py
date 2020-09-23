def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False
    
base = input("Base del triángulo: ")
while not esDecimal(base):
    base = input("Debe ser un número: ")
    
altura = input("Altura del triángulo: ")
while not esDecimal(altura):
    altura = input("Debe ser un número: ")
    
b = float(base)
h = float(altura)
area = b * h / 2

print("Superficie del triángulo: ", round(area,2))
