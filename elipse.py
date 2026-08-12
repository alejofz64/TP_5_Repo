import math
from elemento_grafico import ElementoGrafico
from punto import Punto

class Elipse(ElementoGrafico):
    def __init__(self, colorHex: str, posicionCentro: Punto, nombreCapa: str, radioMayor: float, radioMenor: float):
        super().__init__(colorHex, posicionCentro, nombreCapa)

        # Validamos que los radios sean positivos
        if radioMayor <= 0:
            raise ValueError("El radio mayor debe ser mayor a 0")
        if radioMenor <= 0:
            raise ValueError("El radio menor debe ser mayor a 0")
        if radioMenor > radioMayor:
            raise ValueError("El radio menor no puede ser mayor que el radio mayor")
        self.__radioMayor = radioMayor
        self.__radioMenor = radioMenor

    def get_radioMayor(self) -> float:
        return self.__radioMayor

    def set_radioMayor(self, radioMayor: float):
        self.__radioMayor = radioMayor

    def get_radioMenor(self) -> float:
        return self.__radioMenor

    def set_radioMenor(self, radioMenor: float):
        self.__radioMenor = radioMenor

    def calcular_area(self) -> float:
        return math.pi * self.__radioMayor * self.__radioMenor

    def calcular_perimetro(self) -> float:
        # Usamos una aproximación común para el perímetro de la elipse
        return 2 * math.pi * math.sqrt((self.__radioMayor**2 + self.__radioMenor**2) / 2)

    def escalar(self, factor: float):
        if factor <= 0:
            raise ValueError("El factor de escala debe ser estrictamente mayor a 0.")
        
        self.__radioMayor *= factor
        self.__radioMenor *= factor

    def __str__(self):
        return f"Elipse [RadioMayor: {self.__radioMayor}, RadioMenor: {self.__radioMenor}] - {super().__str__()}"

