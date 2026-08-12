from punto import Punto
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from elipse import Elipse
from circulo import Circulo
from lienzo import Lienzo

rectangulo = Rectangulo(
    colorHex="#4DC238",
    posicionCentro=Punto(3,4),
    nombreCapa="superior",
    ladoMayor=6.1,
    ladoMenor=8.5
)

elipse = Elipse(
    colorHex="#4822B0",  
    posicionCentro=Punto(1,1),
    nombreCapa="inferior",
    radioMayor=4.3,
    radioMenor=2.2
)

cuadrado = Cuadrado(
    colorHex="#AA1717",
    posicionCentro=Punto(10,10),
    nombreCapa="Capa Principal",
    lado=5.0
)

circulo= Circulo(
    colorHex="#BCD407",
    posicionCentro=Punto(5,2),
    nombreCapa="superior",
    radio=6.8
)

lienzo = Lienzo()
lienzo.agregar_elemento(rectangulo)
lienzo.agregar_elemento(cuadrado)
lienzo.agregar_elemento(elipse)
lienzo.agregar_elemento(circulo)

# print("="*10)

# print(rectangulo)
# print(elipse)
# print(cuadrado)
# print(circulo)

# print("="*10)



"""
Aplicamos el filtro de la escala de grises y 
los movemos al punto de origen

"""
lienzo.aplicar_filtro_grises()
lienzo.mover_todos_al_origen()

lienzo.listar_elementos()

"""Calculamos el área y el perimetro total"""

perimetro = lienzo.calcular_perimetro_total()
area = lienzo.calcular_area_total()
print("\n============")
if perimetro:
    print(f"El perimetro tatal es: ",{perimetro})
    print(f"El área total es: ",{area})
else: print("El lienzo esta bacío")