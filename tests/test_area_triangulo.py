"""
Pruebas unitarias para la calculadora del área del triángulo.
"""

import pytest

def calcular_area_triangulo(base, altura):
    if base < 0:
        raise ValueError("La base no puede ser un valor negativo")
    if base == 0:
        raise ValueError("La base no puede ser cero")
    if altura < 0:
        raise ValueError("La altura no puede ser un valor negativo")
    return (base * altura) / 2

class TestCalculadoraTriangulo:
    """Clase de pruebas para la calculadora del área del triángulo."""

    def test_area_calculo_base_5_altura_7(self):
        """Validar el resultado cuando la base sea 5 y la altura sea 7."""
        base = 5
        altura = 7
        area_esperada = 17.5
        resultado = calcular_area_triangulo(base, altura)
        print(f"\nNombre de la prueba: test_area_calculo_base_5_altura_7")
        print(f"Resultado esperado: {area_esperada}")
        print(f"Resultado final: {resultado}")
        assert resultado == area_esperada, f"Esperado {area_esperada}, pero obtuvo {resultado}"

    def test_base_negativa_no_aceptada(self):
        """Validar que no se acepten valores negativos para la base."""
        print("\nNombre de la prueba: test_base_negativa_no_aceptada")
        with pytest.raises(ValueError, match="La base no puede ser un valor negativo"):
            calcular_area_triangulo(-5, 7)
        print("Resultado esperado: ValueError")
        print("Resultado final: ValueError lanzado correctamente")

    def test_altura_negativa_no_aceptada(self):
        """Validar que no se acepten valores negativos para la altura."""
        print("\nNombre de la prueba: test_altura_negativa_no_aceptada")
        with pytest.raises(ValueError, match="La altura no puede ser un valor negativo"):
            calcular_area_triangulo(5, -7)
        print("Resultado esperado: ValueError")
        print("Resultado final: ValueError lanzado correctamente")

    def test_base_cero_no_aceptada(self):
        """Validar que la base no sea cero."""
        print("\nNombre de la prueba: test_base_cero_no_aceptada")
        with pytest.raises(ValueError, match="La base no puede ser cero"):
            calcular_area_triangulo(0, 7)
        print("Resultado esperado: ValueError")
        print("Resultado final: ValueError lanzado correctamente")