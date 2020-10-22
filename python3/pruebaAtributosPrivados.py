class Timido():
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def preguntarNombreConCuidado(self):
        return "Me llamo {}".format(self.__nombre)
    
    