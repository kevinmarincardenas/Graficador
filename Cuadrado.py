from Figura import Figura


class Cuadrado(Figura):
    def __init__(self, lados):
        if len(lados) != 4:
            raise ValueError("Un cuadrado debe tener exactamente 4 lados.")
        for i in range(len(lados)):
            if i > 0:
                if lados[i].calcular_longitud() != lados[i - 1].calcular_longitud():
                    raise ValueError("Los lados no miden lo mismo")
        super().__init__(lados)

    def agregar_lado(self, lado):
        self.get_lados().pop(0)
        if lado.calcular_longitud() != self.get_lados()[0].calcular_longitud():
            raise ValueError("El nuevo lado no tiene la misma longitud que los otros lados.")
        super().agregar_lado(lado)

    def calcular_area(self):
        if len(self.get_lados()) != 4:
            raise ValueError("Un cuadrado debe tener exactamente 4 lados.")
        # Asumimos que todos los lados tienen la misma longitud
        lado = self.get_lados()[0].calcular_longitud()
        return lado * lado
