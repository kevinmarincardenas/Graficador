from Punto import Punto


class Lado:
    def __init__(self, punto_inicial, punto_final):
        self.__punto_inicial = Punto(punto_inicial.get_x(), punto_inicial.get_y())  # Crear Punto con coordenadas
        self.__punto_final = Punto(punto_final.get_x(), punto_final.get_y())

    def __str__(self):
        return f"Lado({self.__punto_inicial}, {self.__punto_final}, Longitud: {self.calcular_longitud()})"

    def calcular_pendiente(self):
        if self.__punto_final.get_x() == self.__punto_inicial.get_x():
            return float('inf')
        else:
            return ((self.__punto_final.get_y() - self.__punto_inicial.get_y()) /
                    (self.__punto_final.get_x() - self.__punto_inicial.get_y()))

    def calcular_longitud(self):
        return self.__punto_inicial.calculardistancia(self.__punto_final)

    def get_punto_inicial(self):
        return self.__punto_inicial

    def get_punto_final(self):
        return self.__punto_final

    def set_punto_inicial(self, punto_inicial):
        self.__punto_inicial = punto_inicial

    def set_punto_final(self, punto_final):
        self.__punto_final = punto_final
