import unittest

from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        print("Realizamos la prueba:")
    
    def test_suma(self):
        print("prueba de suma correcta:")
        calculadora = Calculadora(8,2)
        self.assertEqual(calculadora.suma(), 10, "La suma no es correcta")
     
    def test_suma_erronea(self):
        print("prueba de suma erronea:")
        calculadora = Calculadora(8,2)
        self.assertNotEqual(calculadora.suma(), 11, "La suma es correcta")
           
    def test_resta(self):
        print("prueba de resta correcta:")
        calculadora = Calculadora(8,2)
        self.assertEqual(calculadora.resta(), 6, "La resta no es correcta")
        
    def test_resta_erronea(self):
        print("prueba de resta erronea:")
        calculadora = Calculadora(8,2)
        self.assertNotEqual(calculadora.resta(), 11, "La resta es correcta")
        
    def test_multiplicacion(self):
        print("prueba de multiplicacion correcta:")
        calculadora = Calculadora(8,2)
        self.assertEqual(calculadora.multiplicacion(), 16, "La multiplicacion no es correcta")
    
    def test_multiplicacion_erronea(self):
        print("prueba de multiplicacion erronea:")
        calculadora = Calculadora(8,2)
        self.assertNotEqual(calculadora.multiplicacion(), 11, "La multiplicacion es correcta")
        
    def test_division(self):
        print("prueba de division correcta:")
        calculadora = Calculadora(8,2)
        self.assertEqual(calculadora.division(), 4, "La division no es correcta")
    
    def test_division_erronea(self):
        print("prueba de division erronea:")
        calculadora = Calculadora(8,2)
        self.assertNotEqual(calculadora.division(), 11, "La division es correcta")
        
        
if __name__ == '__main__':
    unittest.main()