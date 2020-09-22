notas=(5,7,9,10,6,8)

def contenido (lista,indice):
    try:
        resultado = lista[indice]
    except:
        resultado = None
        
    return resultado

#Calcular media notas
elemento= 0
suma = 0
while contenido(notas,elemento) != None:
    suma = suma + notas[elemento]
    elemento = elemento + 1

media = suma / elemento

#Salida de resultados
print("     Notas: ", elemento)
print("Suma total: ", suma)
print("Nota media: ", media)