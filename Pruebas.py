from Figura import Figura
from Punto import Punto
from Lado import Lado

punto1 = Punto(0, 0)
punto2 = Punto(2, 4)
punto3 = Punto(4, 0)

lado1 = Lado(punto1, punto2)
lado2 = Lado(punto2, punto3)
lado3 = Lado(punto3, punto1)

lados = [lado1, lado2, lado3]
lados.append(Lado(Punto(0, 0),Punto(3, 3)))
puntos = []
x = 3
y = 5
puntos.append((3, 5))
puntos.append((4, 7))
puntos.append((4, 8))

#print(max(puntos))

figura1 = Figura(lados)

punto4 = Punto(3, 4)
punto5 = Punto(6, 7)
lado5 = Lado(punto4, punto5)
punto4.set_x(4)
print(lado5)

#print(figura1)

#     # 30 30 60 0 90 30 60 60

