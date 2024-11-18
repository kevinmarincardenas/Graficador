from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QBrush, QFont, QIcon
from PyQt6.QtWidgets import QWidget, QGraphicsView, QGraphicsScene, QLabel, QScrollArea
from PyQt6 import uic

from Figura import Figura
from Lado import Lado
from Punto import Punto


class VentanaGrafico(QWidget):
    def __init__(self, puntos):
        super().__init__()
        uic.loadUi('graphic.ui', self)
        self.setWindowTitle("Gráfico")
        self.setWindowIcon(QIcon('imgPlanoCartesiano.png'))

        self.crearGrafico(puntos)

    def crearGrafico(self, puntos):
        graphics_view = self.findChild(QGraphicsView, 'graphicsView')
        scene = QGraphicsScene()
        graphics_view.setScene(scene)
        scroll_area = self.findChild(QScrollArea, 'scrollArea')
        descripcion = QLabel("Hola")
        descripcion.setWordWrap(True)
        descripcion.setStyleSheet("padding: 10px;")
        descripcion.setFont(QFont("Arial", 14))

        scroll_area.setWidget(descripcion)
        colores = [Qt.GlobalColor.red, Qt.GlobalColor.blue,
                   Qt.GlobalColor.green, Qt.GlobalColor.darkMagenta,
                   Qt.GlobalColor.darkYellow, Qt.GlobalColor.darkGray,
                   Qt.GlobalColor.darkGreen]
        lados = []
        cc = 0
        max_dimension = 1

        for i, (x, y) in enumerate(puntos):

            # Dibuja un punto
            if i == 0:
                max_dimension = max(max_dimension, abs(x), abs(y))
            else:
                max_dimension = max(max_dimension, abs(puntos[i][0]), abs(puntos[i][1]))

        graph_heigth = 360
        graph_width = 360
        tamano_grafico = max(graph_heigth, graph_width)
        coeficiente_variacion = int(tamano_grafico / max_dimension / 2)
        scene.addLine(0, graph_heigth / 2, graph_width, graph_heigth / 2, Qt.GlobalColor.black)
        scene.addLine(graph_width / 2, 0, graph_width / 2, graph_heigth, Qt.GlobalColor.black)

        for i in range(0, tamano_grafico, coeficiente_variacion):
            scene.addLine(graph_width / 2 - 3, i, graph_width / 2 + 3, i, Qt.GlobalColor.black)
            scene.addLine(i, graph_heigth / 2 - 3, i, graph_heigth / 2 + 3, Qt.GlobalColor.black)

        for i, (x, y) in enumerate(puntos):
            x_esc = graph_width / 2 + x * coeficiente_variacion
            y_esc = graph_heigth / 2 - y * coeficiente_variacion

            radius = 3
            scene.addEllipse(x_esc - radius, y_esc - radius, radius * 2, radius * 2, QPen(Qt.GlobalColor.black),
                             QBrush(Qt.GlobalColor.black))

            if i > 0:
                lados.append(Lado(Punto(puntos[i-1][0], puntos[i-1][1]),
                                  Punto(puntos[i][0], puntos[i][1])))
                x_prev, y_prev = puntos[i - 1]
                x_prev_esc = graph_width / 2 + x_prev * coeficiente_variacion
                y_prev_esc = graph_heigth / 2 - y_prev * coeficiente_variacion
                scene.addLine(x_prev_esc, y_prev_esc, x_esc, y_esc, QPen(colores[cc]))
                cc = (cc + 1) % len(colores)

        if len(puntos) > 1:
            lados.append(Lado(Punto(puntos[-1][0], puntos[-1][1]),
                              Punto(puntos[0][0], puntos[0][1])))
            scene.addLine(graph_width / 2 + puntos[-1][0] * coeficiente_variacion,
                          graph_heigth / 2 - puntos[-1][1] * coeficiente_variacion,
                          graph_width / 2 + puntos[0][0] * coeficiente_variacion,
                          graph_heigth / 2 - puntos[0][1] * coeficiente_variacion,
                          QPen(colores[cc]))

        figura = Figura(lados)
        descripcion.setText(str(figura))
        print(figura)
