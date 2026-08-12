from elemento_grafico import ElementoGrafico
from punto import Punto

class Rectangulo(ElementoGrafico):
    def __init__(self, colorHex: str, posicionCentro: Punto, nombreCapa: str, ladoMenor: float, ladoMayor: float):
        super().__init__(colorHex, posicionCentro, nombreCapa)
        self.__ladoMenor = ladoMenor
        self.__ladoMayor = ladoMayor

    def get_ladoMenor(self) -> float:
        return self.__ladoMenor

    def set_ladoMenor(self, ladoMenor: float):
        self.__ladoMenor = ladoMenor

    def get_ladoMayor(self) -> float:
        return self.__ladoMayor

    def set_ladoMayor(self, ladoMayor: float):
        self.__ladoMayor = ladoMayor

    def calcular_area(self) -> float:
        return self.__ladoMenor * self.__ladoMayor

    def calcular_perimetro(self) -> float:
        return 2 * (self.__ladoMenor + self.__ladoMayor)

    def escalar(self, factor: float):
        if factor <= 0:
            raise ValueError("El factor de escala debe ser estrictamente mayor a 0.")
        
        self.__ladoMenor *= factor
        self.__ladoMayor *= factor

    def __str__(self):
        return f"Rectangulo [LadoMenor: {self.__ladoMenor}, LadoMayor: {self.__ladoMayor}] - {super().__str__()}"

