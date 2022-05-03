# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import espar

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_par(self):
        assert espar(4) == True
        assert espar(75) == False
        assert espar(100) == True
        assert espar(99) == False
