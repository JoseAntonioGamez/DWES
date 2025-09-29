class animal():
    
    def __init__(self,nombre = ""):
        self.nombre=nombre
    
    def mostrarnombre(self):
        return self.nombre

   # def __str__(self):
    #    return "Nombre: ", self.nombre

class perro(animal):
    
    def __init__(self):
        super().__init__("perro")

class gato(animal):
    
    def __init__(self):
        self.nombre = "gato"

animal1= animal("perro")
animal2 = animal("gato")    
animal3 = animal("cerdo")



animal1.mostrarnombre()
animal2.mostrarnombre()
animal3.mostrarnombre()

