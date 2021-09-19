import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtCore import QPoint, Qt


class Calculadora(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.grid_layout = QGridLayout()
        self.line_edit = QLineEdit()
        self.oldPos = self.pos()

        self.initialize_ui()

    def initialize_ui(self):
        self.setFixedSize(300, 400)
        self.setWindowTitle("Pycalc")
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.grid_layout.setContentsMargins(0,0,0,0)
        self.grid_layout.setSpacing(0)

        close_btn = QtWidgets.QToolButton(self)
        close_btn.clicked.connect(self.close)
        close_btn.setMinimumHeight(20)
        close_btn.setMinimumWidth(30)
        close_btn.setText("X")
        
        self.grid_layout.addWidget(close_btn, 0,0,1,1)

        css = """
        QWidget{
            Background: #a8735c;
            color:white;
            font:18px bold;
            font-weight:bold;
            font-family: 'Century Gothic';
            border-radius: 1px;
        }
        QToolButton{
            Background:#ec3430;
            font-size:11px;
        }
        QToolButton:hover{
            Background: #fb5652;
        }
        QLineEdit{
            color: #fff1e3;
            font-size: 40px;
            font-weight: normal;
            font-family: 'Century Gothic', 'Sans Serif';
        }
        QPushButton{
            background: #d6d6d6;
            color: #313131;
            border:1px solid #b2aead;
        }
        """
        self.setStyleSheet(css)

        self.line_edit.setDisabled = True
        self.line_edit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grid_layout.addWidget(self.line_edit, 1, 0, 1, 4)

        self.add_button(QPushButton("C"), 2, 0, 1, 1, lambda: self.line_edit.setText(""))
        self.add_button(QPushButton("<"), 2, 1,1,1,lambda: self.line_edit.setText(self.line_edit.text()[:-1]),)
        self.add_button(QPushButton("%"), 2, 2, 1, 1, self.percentage)
        self.add_button(QPushButton("÷"), 2, 3, 1, 1, style=True)

        self.add_button(QPushButton("7"), 3, 0, 1, 1)
        self.add_button(QPushButton("8"), 3, 1, 1, 1)
        self.add_button(QPushButton("9"), 3, 2, 1, 1)
        self.add_button(QPushButton("x"), 3, 3, 1, 1,style=True)

        self.add_button(QPushButton("4"), 4, 0, 1, 1)
        self.add_button(QPushButton("5"), 4, 1, 1, 1)
        self.add_button(QPushButton("6"), 4, 2, 1, 1)
        self.add_button(QPushButton("-"), 4, 3, 1, 1,style=True)

        self.add_button(QPushButton("1"), 5, 0, 1, 1)
        self.add_button(QPushButton("2"), 5, 1, 1, 1)
        self.add_button(QPushButton("3"), 5, 2, 1, 1)
        self.add_button(QPushButton("+"), 5, 3, 1, 1,style=True)

        self.add_button(QPushButton("0"), 6, 0, 1, 2)
        self.add_button(QPushButton("."), 6, 2, 1, 1)
        self.add_button(QPushButton("="), 6, 3, 1, 1, self.calculate,True)

        self.setLayout(self.grid_layout)
        self.show()

    def add_button(self, button, row, col, rowspan, colspan, function=None, style=None):
        self.grid_layout.addWidget(button, row, col, rowspan, colspan)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        if not function:
            button.clicked.connect(
                lambda: self.line_edit.setText(self.line_edit.text() + button.text())
            )
        else:
            button.clicked.connect(function)
        if style:
            button.setStyleSheet("* {background: #f5923d; color: white; border:1px solid #cf884a;}")


    def calculate(self):
        to_eval = self.line_edit.text().replace("x", "*")
        to_eval = to_eval.replace("÷", "/")
        try:
            self.line_edit.setText(str(eval(to_eval)))
        except Exception as e:
            self.line_edit.setText("Value Error")

    def percentage(self):
        if "÷" in self.line_edit.text():
            try:
                num, percent = self.line_edit.text().split("÷")
                num, percent = float(num), float(percent)
                result = num / (percent/100)
                self.line_edit.setText(str(self.safe_to_int(result)))
            except Exception as e:
                self.line_edit.setText("Value Error")

        if "x" in self.line_edit.text():
            try:
                num, percent = self.line_edit.text().split("x")
                num, percent = float(num), float(percent)
                result = (num / 100) * percent
                self.line_edit.setText(str(self.safe_to_int(result)))
            except Exception as e:
                self.line_edit.setText("Value Error")
        if "-" in self.line_edit.text():
            try:
                num, percent = self.line_edit.text().split("-")
                num, percent = float(num), float(percent)
                result = num - (num / 100) * percent
                self.line_edit.setText(str(self.safe_to_int(result)))
            except Exception as e:
                self.line_edit.setText("Value Error")

        if "+" in self.line_edit.text():
            try:
                num, percent = self.line_edit.text().split("+")
                num, percent = float(num), float(percent)
                result = num + (num / 100) * percent
                self.line_edit.setText(str(self.safe_to_int(result)))
            except Exception as e:
                print(e)
                self.line_edit.setText("Value Error")
    
    def safe_to_int(self, num):
        print(num)
        if int(num) == num:
            return int(num)
        return num
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculadora()
    sys.exit(app.exec_())
