class FiguraGeometrica():
    def __init__(self,ancho=0, altura=0):
        self.ancho=ancho
        self.altura=altura
    
    
    def area(self):
        return self.ancho*self.altura
    
    class Rectangulo(FiguraGeometrica):
        def area(self):
            super().__init__()
            return self.ancho, self.altura