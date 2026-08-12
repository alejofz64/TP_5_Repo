from elemento_grafico import ElementoGrafico
from punto import Punto

class Cuadrado(ElementoGrafico):
    def __init__(self, colorHex: str, posicionCentro: Punto, nombreCapa: str, lado: float):
        # Invocamos al constructor de la clase base
        super().__init__(colorHex, posicionCentro, nombreCapa)
        
        # Validamos que el lado sea positivo
        if lado <= 0:
            raise ValueError("El lado debe ser mayor a 0")
        
        self.__lado = lado

    def get_lado(self) -> float:
        return self.__lado

    def set_lado(self, lado: float):
        # Validamos que el nuevo lado sea positivo
        if lado <= 0:
            raise ValueError("El lado debe ser mayor a 0")
        self.__lado = lado

    def calcular_area(self) -> float:
        """Calcula el área del cuadrado: lado * lado"""
        return self.__lado ** 2

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del cuadrado: 4 * lado"""
        return 4 * self.__lado

    def escalar(self, factor: float):
        if factor <= 0:
            raise ValueError("El factor de escala debe ser estrictamente mayor a 0. "
                           "Un factor <= 0 resultaría en un cuadrado sin dimensiones "
                           "válidas (lado = 0 o negativo).")
        
        self.__lado *= factor

    def __str__(self):
        """
        Sobrescribe el método __str__() invocando internamente a super().__str__()
        para aprovechar el código de la clase base.
        """
        return f"Cuadrado [Lado: {self.__lado}] - {super().__str__()}"

