import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QPushButton, QScrollArea, QSpinBox
from PyQt6 import uic
from VentanaGrafico import VentanaGrafico


class VentanaDinamica(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('userinterface.ui', self)

        self.ui_spinBox = self.findChild(QSpinBox, 'spinBox')
        self.ui_scrollArea = self.findChild(QScrollArea, 'scrollArea_3')
        self.ui_scrollAreaGraphics = self.findChild(QScrollArea, 'scrollArea_2')
        self.ui_scrollAreaWidgetContents = self.ui_scrollArea.widget()
        self.ui_gridLayout = QGridLayout(self.ui_scrollAreaWidgetContents)

        # Cargar el botón y conectar la señal
        self.ui_btnCrearGrafico = self.findChild(QPushButton, 'btnCrearGrafico')
        self.ui_btnCrearGrafico.clicked.connect(self.crear_grafico)

        self.ui_spinBox.valueChanged.connect(self.actualizar_labels)

        self.labels = []
        self.x_inputs = []
        self.y_inputs = []

    def actualizar_labels(self, valor):
        while len(self.labels) < valor:
            punto_label = QLabel(f"Punto {len(self.labels) + 1}", self)
            x_label = QLabel("x=", self)
            x_input = QLineEdit(self)
            y_label = QLabel("y=", self)
            y_input = QLineEdit(self)

            self.labels.append((punto_label, x_label, y_label))
            self.x_inputs.append(x_input)
            self.y_inputs.append(y_input)

            fila = len(self.labels) - 1
            self.ui_gridLayout.addWidget(punto_label, fila, 0)
            self.ui_gridLayout.addWidget(x_label, fila, 1)
            self.ui_gridLayout.addWidget(x_input, fila, 2)
            self.ui_gridLayout.addWidget(y_label, fila, 3)
            self.ui_gridLayout.addWidget(y_input, fila, 4)

        while len(self.labels) > valor:
            punto_label, x_label, y_label = self.labels.pop()
            x_input = self.x_inputs.pop()
            y_input = self.y_inputs.pop()

            punto_label.deleteLater()
            x_label.deleteLater()
            x_input.deleteLater()
            y_label.deleteLater()
            y_input.deleteLater()

        # Actualizar textos de labels
        for i in range(len(self.labels)):
            self.labels[i][0].setText(f"Punto {i + 1}")

    def crear_grafico(self):
        # Obtener los puntos de los QLineEdit
        puntos = []
        for x_input, y_input in zip(self.x_inputs, self.y_inputs):
            try:
                x = float(x_input.text())
                y = (float(y_input.text()))
                puntos.append((x, y))
            except ValueError:
                continue  # Ignorar entradas no válidas

        # Crear y mostrar la ventana del gráfico
        self.ventana_grafico = VentanaGrafico(puntos)
        self.ventana_grafico.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaDinamica()
    ventana.show()
    sys.exit(app.exec())
