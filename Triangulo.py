import math

from Figura import Figura


class Triangulo(Figura):
    def __init__(self, lados):
        if len(lados) != 3:
            raise ValueError("Un Triángulo debe tener exactamente 3 lados.")
        super().__init__(lados)

    def agregar_lado(self, lado):
        self.get_lados().pop(0)
        super().agregar_lado(lado)

    def calcular_area(self):
        if len(self.get_lados()) != 3:
            raise ValueError("Un triángulo debe tener exactamente 3 lados.")

        a = self.get_lados()[0].calcular_longitud()
        b = self.get_lados()[1].calcular_longitud()
        c = self.get_lados()[2].calcular_longitud()

        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return round(area, 2)
