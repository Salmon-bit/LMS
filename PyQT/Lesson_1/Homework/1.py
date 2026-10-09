from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLineEdit, QLabel)
import sys


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 290, 50)
        self.setWindowTitle("Арифмометр")

        self.first_value = QLineEdit(self)
        self.first_value.setText('0')
        self.first_value.resize(50, 20)
        self.first_value.move(5, 5)

        self.add_button = QPushButton('+', self)
        self.substract_button = QPushButton('-', self)
        self.multiply_button = QPushButton('*', self)

        self.add_button.resize(20, 20)
        self.substract_button.resize(20, 20)
        self.multiply_button.resize(20, 20)
        self.add_button.move(60, 5)
        self.substract_button.move(80, 5)
        self.multiply_button.move(100, 5)

        self.second_value = QLineEdit(self)
        self.second_value.setText('0')
        self.second_value.resize(50, 20)
        self.second_value.move(125, 5)

        lb = QLabel('=', self)
        lb.resize(20, 20)
        lb.move(180, 5)

        self.result = QLineEdit(self)
        self.result.setText('0')
        self.result.resize(50, 20)
        self.result.move(195, 5)
        self.result.setDisabled(True)
        
        self.add_button.clicked.connect(self.count)
        self.substract_button.clicked.connect(self.count)
        self.multiply_button.clicked.connect(self.count)

    def count(self):
        sender = self.sender()

        if sender.text() == '+':
            self.result.setText(str(int(self.first_value.text()) + int(self.second_value.text())))
        elif sender.text() == '*':
            self.result.setText(str(int(self.first_value.text()) * int(self.second_value.text())))
        elif sender.text() == '-':
            self.result.setText(str(int(self.first_value.text()) - int(self.second_value.text())))


if __name__ == "__main__":
    ap = QApplication(sys.argv)
    ar = Arifmometr()
    ar.show()
    sys.exit(ap.exec())
