class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso >=8:
            print("GUAU GUAU")
        else:
            print("Guau, Guau")
            
    def __str__(self):
        return "Perro {}, edad: {}, peso: {}".format(self.nombre,self.edad,self.peso)
    
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
        
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)
    
    def pasear(self):
        print("{} ayuda a su dueño, {}, a pasear".format(self.nombre, self.amo))
        
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor

    def ladrar(self):
        if self.__trabajando:
            print("Shhh, no puedo ladrar")
        else:
            Perro.ladrar(self)

    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
            