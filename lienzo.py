from elemento_grafico import ElementoGrafico
from punto import Punto
from typing import List

class Lienzo:
    def __init__(self):
        """Inicializa un lienzo """
        self.__elementos: List[ElementoGrafico] = []

    def agregar_elemento(self, elemento: ElementoGrafico):
        """
        Agrega un elemento gráfico al lienzo
        
        """
        if elemento is None:
            raise ValueError("No se puede agregar un elemento nulo al lienzo")
        self.__elementos.append(elemento)

    def eliminar_elemento(self, elemento: ElementoGrafico):
        """
        Elimina un elemento gráfico del lienzo
        
        """
        if elemento in self.__elementos:
            self.__elementos.remove(elemento)
        else:
            raise ValueError("El elemento no existe en el lienzo")

    def obtener_elementos(self) -> List[ElementoGrafico]:
        """Retorna una copia de la lista de elementos"""
        return self.__elementos.copy()

    def obtener_cantidad_elementos(self) -> int:
        """Retorna la cantidad de elementos en el lienzo"""
        return len(self.__elementos)
    
    def calcular_area_total(self) -> float:
        """
        Calcula la suma de las áreas de todos los elementos del lienzo.
        AHORA FUNCIONA gracias a que ElementoGrafico es abstracta y
        define calcular_area() como método abstracto.
        """
        area_total = 0.0
        for elemento in self.__elementos:
            area_total += elemento.calcular_area()
        return area_total

    def calcular_perimetro_total(self) -> float:
        """Calcula la suma de los perímetros de todos los elementos"""
        perimetro_total = 0.0
        for elemento in self.__elementos:
            perimetro_total += elemento.calcular_perimetro()  
        return perimetro_total


    def aplicar_filtro_grises(self):
        """
        Aplica un filtro de escala de grises a todos los elementos del lienzo
        Cambia el color de todos los elementos a #808080
        """
        for elemento in self.__elementos:
            elemento.set_colorHex("#808080")

    def mover_todos_al_origen(self):
        """
        Mueve todos los elementos del lienzo al punto (0,0)
        """
        origen = Punto(0, 0)
        for elemento in self.__elementos:
            elemento.moverA(origen)

    def listar_elementos(self):
        """Muestra todos los elementos del lienzo con su información"""
        if not self.__elementos:
            print("El lienzo está vacío")
            return
        
        print(f"\n{'='*60}")
        print(f"LIENZO - Total de elementos: {len(self.__elementos)}")
        print(f"{'='*60}")
        
        for i, elemento in enumerate(self.__elementos, 1):
            print(f"{i}. {elemento.__str__()}")

    def __str__(self):
        return f"Lienzo [Cantidad de elementos: {len(self.__elementos)}]"