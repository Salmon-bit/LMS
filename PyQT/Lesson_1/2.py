import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 370, 65)
        self.setWindowTitle('Вычисление выражений')

        self.first_value = QLineEdit(self)
        self.first_value.resize(150, 30)
        self.second_value = QLineEdit(self)
        self.second_value.resize(150, 30)
        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(50, 30)
        self.i_text_l = QLabel(self)
        self.i_text_l.setText('Выражение:')
        self.o_text_l = QLabel(self)
        self.o_text_l.setText('Результат:')
        self.first_value.move(5, 25)
        self.trick_button.move(160, 25)
        self.second_value.move(215, 25)
        self.i_text_l.move(5, 5)
        self.o_text_l.move(215, 5)
        self.trick_button.clicked.connect(self.trick)

    def trick(self):
        self.second_value.setText(str(eval(self.first_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.show()
    sys.exit(app.exec())
