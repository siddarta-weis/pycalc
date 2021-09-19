import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.grid_layout = QGridLayout()
        self.line_edit = QLineEdit()

        self.initialize_ui()

    def initialize_ui(self):
        self.setFixedSize(300, 400)
        self.setWindowTitle("Pycalc")

        self.line_edit.setDisabled = True
        self.line_edit.setStyleSheet(
            "* {background: #a67960; color: #eee; font-size: 30px;}"
        )
        self.line_edit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.grid_layout.addWidget(self.line_edit, 0, 0, 1, 4)

        self.add_button(
            QPushButton("C"), 1, 0, 1, 1, lambda: self.line_edit.setText("")
        )
        self.add_button(
            QPushButton("<"),
            1,
            1,
            1,
            1,
            lambda: self.line_edit.setText(self.line_edit.text()[:-1]),
        )
        self.add_button(QPushButton("%"), 1, 2, 1, 1, self.percentage)
        self.add_button(QPushButton("÷"), 1, 3, 1, 1)

        self.add_button(QPushButton("7"), 2, 0, 1, 1)
        self.add_button(QPushButton("8"), 2, 1, 1, 1)
        self.add_button(QPushButton("9"), 2, 2, 1, 1)
        self.add_button(QPushButton("x"), 2, 3, 1, 1)

        self.add_button(QPushButton("4"), 3, 0, 1, 1)
        self.add_button(QPushButton("5"), 3, 1, 1, 1)
        self.add_button(QPushButton("6"), 3, 2, 1, 1)
        self.add_button(QPushButton("-"), 3, 3, 1, 1)

        self.add_button(QPushButton("1"), 4, 0, 1, 1)
        self.add_button(QPushButton("2"), 4, 1, 1, 1)
        self.add_button(QPushButton("3"), 4, 2, 1, 1)
        self.add_button(QPushButton("+"), 4, 3, 1, 1)

        self.add_button(QPushButton("0"), 5, 0, 1, 2)
        self.add_button(QPushButton("."), 5, 2, 1, 1)
        self.add_button(QPushButton("="), 5, 3, 1, 1, self.eval_igual)

        self.setLayout(self.grid_layout)
        self.show()

    def add_button(self, button, row, col, rowspan, colspan, function=None):
        self.grid_layout.addWidget(button, row, col, rowspan, colspan)
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        if not function:
            button.clicked.connect(
                lambda: self.line_edit.setText(self.line_edit.text() + button.text())
            )
        else:
            button.clicked.connect(function)

    def eval_igual(self):
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculadora()
    sys.exit(app.exec_())
