import math

from Cuadrado import Cuadrado
from Figura import Figura
from Lado import Lado
from Punto import Punto
from Triangulo import Triangulo


punto1 = Punto(1, 1)
punto2 = Punto(1, 4)
punto3 = Punto(4,  4)
punto4 = Punto(4, 1)

lado1 = Lado(punto1, punto2)
lado2 = Lado(punto2, punto3)
lado3 = Lado(punto3, punto4)
lado4 = Lado(punto4, punto1)
lado5 = Lado(punto3, punto1)

lados_cuadrado = [lado1, lado2, lado3, lado4]
lados_triangulo = [lado1, lado2, lado5]

cuadrado1 = Cuadrado(lados_cuadrado)
triangulo1 = Triangulo(lados_triangulo)
figuras = [cuadrado1, triangulo1]

for i in range(len(figuras)):
    print("Figura "+str(i+1)+":")
    print("Perímetro: "+str(figuras[i].calcular_perimetro()))
    print("Área: "+str(figuras[i].calcular_area())+"\n")


