def myUpper(cadena):
    resultado = ""
    
    for caracter in cadena:
        codigoCaracter = ord(caracter)
        if codigoCaracter >= 97 and codigoCaracter <= 122:
            codigoMays = codigoCaracter - 32
            caracterMays = chr(codigoMays)
            resultado += caracterMays
        else:
            resultado += caracter
        
    return resultado

palabras = input("Dime algo bajito: ")
print("Te grito:", myUpper(palabras))
