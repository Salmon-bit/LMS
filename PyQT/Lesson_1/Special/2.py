import sys
from random import randint
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLCDNumber)


class NimStrikesBack(QWidget):
    def __init__(self):
        super().__init__()

        self.x = randint(1, 50)
        self.y = randint(1, 10)
        self.z = randint(1, 10)
        self.steps = 10

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Ним Наносит Ответный Удар!')

        self.result_label = QLabel('', self)
        self.result_label.resize(300, 20)
        self.result_label.move(5, 5)

        self.btnp = QPushButton('+' + str(self.y), self)
        self.btnm = QPushButton('-' + str(self.z), self)
        self.btnp.clicked.connect(self.step)
        self.btnm.clicked.connect(self.step)

        self.steps_left_lb = QLabel('Осталось ходов:', self)
        self.current_num_lb = QLabel('Текущее число:', self)
        self.steps_left_lcd = QLCDNumber(self)
        self.current_num_lcd = QLCDNumber(self)

        self.steps_left_lcd.display(str(self.steps))
        self.current_num_lcd.display(str(self.x))

        self.btnp.resize(100, 30)
        self.btnm.resize(100, 30)

        self.btnp.move(50, 50)
        self.btnm.move(150, 50)

        self.steps_left_lb.move(20, 95)
        self.current_num_lb.move(20, 140)

        self.steps_left_lcd.resize(100, 30)
        self.current_num_lcd.resize(100, 30)

        self.steps_left_lcd.move(180, 91)
        self.current_num_lcd.move(180, 137)

    def step(self):
        self.x = int(eval(f'{self.x}{self.sender().text()}'))
        self.steps -= 1

        if (self.steps <= 0):
            if self.x != 0:
                self.result_label.setText('Вы проиграли, начинаем новую игру')
            else:
                self.result_label.setText('Вы победили, начинаем новую игру')
            self.restart()
            return

        if self.result_label.text() != '':
            self.result_label.setText('')

        self.steps_left_lcd.display(str(self.steps))
        self.current_num_lcd.display(str(self.x))

    def restart(self):
        self.x = randint(1, 50)
        self.y = randint(0, 10)
        self.z = randint(0, 10)
        self.steps = 10

        self.steps_left_lcd.display(str(self.steps))
        self.current_num_lcd.display(str(self.x))

        self.btnp.setText('+' + str(self.y))
        self.btnm.setText('-' + str(self.z))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    nsb = NimStrikesBack()
    nsb.show()
    sys.exit(app.exec())
