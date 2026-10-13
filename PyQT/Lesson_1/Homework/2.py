from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton)
import sys


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()

        self.alphabet = 'abcdefgijklmnopqrstuvwxyz'
        self.morse_dic = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '-.-',
            's': '...',
            't': '-',
            'u': '--.',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..'
        }
        self.alphabet_buttons = {}

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Азбука Морзе")
        self.setGeometry(300, 300, 310, 75)

        for i in range(len(self.alphabet)):
            b = QPushButton(self.alphabet[i], self)
            b.resize(20, 20)
            b.move(5 + (i % 15) * 20, 5 if i < 15 else 25)
            b.clicked.connect(self.click)

            self.alphabet_buttons[self.alphabet[i]] = b

        self.result = QLineEdit(self)
        self.result.resize(300, 20)
        self.result.move(5, 50)

    def click(self):
        s = self.sender()
        self.result.setText(self.result.text() + self.morse_dic.get(s.text(), ''))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MorseCode()
    mc.show()
    sys.exit(app.exec())
