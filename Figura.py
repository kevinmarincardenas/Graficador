from abc import abstractmethod


class Figura:
    def __init__(self, lados):
        self.__lados = lados

    def agregar_lado(self, lado):
        self.__lados.append(lado)

    def __str__(self):
        descripcion = f"Figura con {len(self.__lados)} lados y Perímetro: {self.calcular_perimetro()}\n"
        descripcion += "Lados:\n"
        for i, lado in enumerate(self.__lados, start=1):
            descripcion += f"Lado {i}: {lado}\n"
        return descripcion

    def calcular_perimetro(self):
        perimetro = 0
        for lado in self.__lados:
            perimetro += lado.calcular_longitud()
        return round(perimetro, 2)

    def get_lados(self):
        return self.__lados

    @abstractmethod
    def calcular_area(self):
        pass
