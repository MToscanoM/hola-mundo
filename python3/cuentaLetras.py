miTexto = "Cuatro palabras para ti."

frecuencias = dict()

for caracter in miTexto:
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1
        
for clave in frecuencias.keys():
    print(clave, "-", frecuencias[clave])
    
        