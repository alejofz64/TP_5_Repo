import math
from elemento_grafico import ElementoGrafico
from punto import Punto

class Circulo(ElementoGrafico):
    def __init__(self, colorHex: str, posicionCentro: Punto, nombreCapa: str, radio: float):
        super().__init__(colorHex, posicionCentro, nombreCapa)
        
        # Validamos que el radio sea positivo
        if radio <= 0:
            raise ValueError("El radio debe ser mayor a 0")
        
        self.__radio = radio

    def get_radio(self) -> float:
        return self.__radio

    def set_radio(self, radio: float):
        # Validamos que el nuevo radio sea positivo
        if radio <= 0:
            raise ValueError("El radio debe ser mayor a 0")
        self.__radio = radio

    def calcular_area(self) -> float:
        """Calcula el área del círculo: π * radio²"""
        return math.pi * (self.__radio ** 2)

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro (circunferencia) del círculo: 2 * π * radio"""
        return 2 * math.pi * self.__radio

    def escalar(self, factor: float):
        if factor <= 0:
            raise ValueError("El factor de escala debe ser estrictamente mayor a 0. "
                           "Un factor <= 0 resultaría en un círculo sin dimensiones "
                           "válidas (radio = 0 o negativo).")
        
        self.__radio *= factor

    def obtener_diametro(self) -> float:
        """Calcula el diámetro del círculo: 2 * radio"""
        return 2 * self.__radio

    def __str__(self):
        return f"Circulo [Radio: {self.__radio}] - {super().__str__()}"

