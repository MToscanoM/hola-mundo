notas=(5,7,9,10,6,8)

longNotas = len(notas)

#Calcular media notas
suma = 0
for indice in range(0,longNotas):
    suma = suma + notas[indice]
    
media = suma / longNotas

#Salida de resultados
print("     Notas: ", longNotas)
print("Suma total: ", suma)
print("Nota media: ", media)