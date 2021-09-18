import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Pycalc")
        self.setFixedSize(300, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw, spacing=0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    app.exec_()
