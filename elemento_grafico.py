from abc import ABC, abstractmethod
from punto import Punto

class ElementoGrafico(ABC):
    def __init__(self, colorHex: str, posicionCentro: Punto, nombreCapa: str):
        self.__colorHex = colorHex
        self.__posicionCentro = posicionCentro
        self.__nombreCapa = nombreCapa

    def get_colorHex(self):
        return self.__colorHex

    def set_colorHex(self, colorHex):
        self.__colorHex = colorHex

    def get_posicionCentro(self):
        return self.__posicionCentro

    def set_posicionCentro(self, posicionCentro: Punto):
        self.__posicionCentro = posicionCentro

    def get_nombreCapa(self):
        return self.__nombreCapa

    def set_nombreCapa(self, nombreCapa):
        self.__nombreCapa = nombreCapa

    def moverA(self, nuevoDestino: Punto):
        self.__posicionCentro = nuevoDestino

    @abstractmethod
    def calcular_area(self) -> float:
        pass

    @abstractmethod
    def calcular_perimetro(self) -> float:
        pass

    @abstractmethod
    def escalar(self,factor: float):
        pass


    def __str__(self):
        return f"ElementoGrafico(Capa='{self.__nombreCapa}', Color='{self.__colorHex}', Centro={self.__posicionCentro.__str__()})"

