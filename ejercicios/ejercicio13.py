class Estudiante():
    def __init__(self,nombre="", edad=0, curso=""):
        self.nombre=nombre
        self.edad=edad
        self.curso=curso
        
estudiante1= Estudiante("Paco", "13", "1ºDAW")
estudiante2 = Estudiante("Lucia", "15", "2ºDAW")    
estudiante3 = Estudiante("Carlos", "14", "1ºASIR")

lista=[estudiante1, estudiante2, estudiante3]
for estu in lista:
    print(estu.nombre, estu.edad, estu.curso)