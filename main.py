import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        
        
        self.initialize_ui()

    def initialize_ui(self):
        self.setFixedSize(300, 400)
        self.setWindowTitle("Pycalc")
        
        line_edit = QLineEdit()
        line_edit.setDisabled = True
        line_edit.setStyleSheet("* {background: #a67960; color: #eee; font-size: 30px;}")
        line_edit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        grid_layout = QGridLayout()
        grid_layout.addWidget(line_edit, 0,0,1,4)

        self.add_button(grid_layout ,QPushButton("C"),line_edit,1,0,1,1,lambda: line_edit.setText(""))
        self.add_button(grid_layout ,QPushButton("<"),line_edit,1,1,1,1)
        self.add_button(grid_layout ,QPushButton("%"),line_edit,1,2,1,1)
        self.add_button(grid_layout ,QPushButton("÷"),line_edit,1,3,1,1)
        
        self.add_button(grid_layout ,QPushButton("7"),line_edit,2,0,1,1)
        self.add_button(grid_layout ,QPushButton("8"),line_edit,2,1,1,1)
        self.add_button(grid_layout ,QPushButton("9"),line_edit,2,2,1,1)
        self.add_button(grid_layout ,QPushButton("x"),line_edit,2,3,1,1)
        
        self.add_button(grid_layout ,QPushButton("4"),line_edit,3,0,1,1)
        self.add_button(grid_layout ,QPushButton("5"),line_edit,3,1,1,1)
        self.add_button(grid_layout ,QPushButton("6"),line_edit,3,2,1,1)
        self.add_button(grid_layout ,QPushButton("-"),line_edit,3,3,1,1)
        
        self.add_button(grid_layout ,QPushButton("4"),line_edit,4,0,1,1)
        self.add_button(grid_layout ,QPushButton("5"),line_edit,4,1,1,1)
        self.add_button(grid_layout ,QPushButton("6"),line_edit,4,2,1,1)
        self.add_button(grid_layout ,QPushButton("-"),line_edit,4,3,1,1)
        
        self.add_button(grid_layout ,QPushButton("0"),line_edit,5,0,1,2)
        self.add_button(grid_layout ,QPushButton("."),line_edit,5,2,1,1)
        self.add_button(grid_layout ,QPushButton("="),line_edit,5,3,1,1, self.eval_igual(line_edit))



        self.setLayout(grid_layout)
        self.show()
    
    def add_button(self,grid_layout, button, line_edit, row, col, rowspan, colspan, function=None):
        grid_layout.addWidget(button, row, col, rowspan, colspan)
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        if not function:
            button.clicked.connect(
                lambda: line_edit.setText(line_edit.text() + button.text())
            )
        else:
            button.clicked.connect(function)
    
    def eval_igual(self, line_edit):
        try:
            line_edit.setText(str(eval(line_edit.text())))
        except Exception as e:
            line_edit.setText('Conta errada')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculadora()
    sys.exit(app.exec_())
