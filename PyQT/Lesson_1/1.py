import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


class WordTrick(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.side = 'r_to_l'

    def initUI(self):
        self.setGeometry(300, 300, 350, 30)
        self.setWindowTitle('Фокус над словами')

        self.first_value = QLineEdit(self)
        self.first_value.resize(150, 30)
        self.second_value = QLineEdit(self)
        self.second_value.resize(150, 30)
        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(50, 30)
        self.first_value.move(0, 0)
        self.trick_button.move(150, 0)
        self.second_value.move(200, 0)
        self.trick_button.clicked.connect(self.trick)

    def trick(self):
        if self.side == 'r_to_l':
            self.second_value.setText(self.first_value.text())
            self.first_value.setText('')
            self.side = 'l_to_r'
            self.trick_button.setText('<-')
        else:
            self.first_value.setText(self.second_value.text())
            self.second_value.setText('')
            self.side = 'r_to_l'
            self.trick_button.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())
