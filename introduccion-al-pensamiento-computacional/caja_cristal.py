import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return False
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)
    
    def test_es_menor_de_edad(self):
        edad = 15
    
        resultado = es_mayor_de_edad(edad)
    
        self.assertEqual(resultado, False)

if __name__ == '__main__':
    unittest.main()