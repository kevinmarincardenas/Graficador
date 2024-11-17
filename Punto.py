import math


class Punto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Punto({self.__x}, {self.__y})"

    def calculardistancia(self, otropunto):
        distancia = math.sqrt(math.pow(self.__x - otropunto.get_x(), 2) + math.pow(self.__y - otropunto.get_y(), 2))
        distancia = int(distancia*100) / 100
        return distancia

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y
