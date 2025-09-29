class Calculadora():
    def __init__(self,num1, num2):
        self.num1=num1
        self.num2=num2
    
    def suma(self):
        return self.num1+self.num2
    
    def resta(self):
        return self.num1-self.num2
    
    def multiplicacion(self):
        return self.num1*self.num2
    
    def division(self):
        return self.num1/self.num2
    
numeros=Calculadora(8,2)

print("La suma es ", Calculadora.suma(numeros))
print("La resta es ", Calculadora.resta(numeros))
print("La multiplicacion es ", Calculadora.multiplicacion(numeros))
print("La division es ", Calculadora.division(numeros))