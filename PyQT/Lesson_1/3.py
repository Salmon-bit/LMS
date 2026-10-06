import sys
from PyQt6.QtWidgets import QApplication,QWidget, QLineEdit
from PyQt6.QtWidgets import QPushButton, QLabel, QLCDNumber


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 370, 145)
        self.setWindowTitle('Миникалькулятор')

        f_num_l = QLabel(self)
        f_num_l.setText('Первое число (целое):')
        f_num_l.move(5, 10)

        self.number_1 = QLineEdit(self)
        self.number_1.resize(100, 20)
        self.number_1.move(5, 30)

        s_num_l = QLabel(self)
        s_num_l.setText('Второе число (целое):')
        s_num_l.move(5, 90)

        self.number_2 = QLineEdit(self)
        self.number_2.resize(100, 20)
        self.number_2.move(5, 115)

        self.calculate_button = QPushButton('->', self)
        self.calculate_button.resize(50, 30)
        self.calculate_button.move(105, 55)
        self.calculate_button.clicked.connect(self.calculate)

        sum_l = QLabel(self)
        sum_l.setText('Сумма:')
        dif_l = QLabel(self)
        dif_l.setText('Разность:')
        mul_l = QLabel(self)
        mul_l.setText('Произведение:')
        div_l = QLabel(self)
        div_l.setText('Частное:')

        self.result_sum = QLCDNumber(self)
        self.result_sum.display(0)
        self.result_sub = QLCDNumber(self)
        self.result_sub.display(0)
        self.result_mul = QLCDNumber(self)
        self.result_mul.display(0)
        self.result_div = QLCDNumber(self)
        self.result_div.display(0)

        self.result_sum.resize(100, 30)
        self.result_sub.resize(100, 30)
        self.result_mul.resize(100, 30)
        self.result_div.resize(100, 30)

        self.result_sum.move(265, 5)
        self.result_sub.move(265, 40)
        self.result_mul.move(265, 75)
        self.result_div.move(265, 110)

        sum_l.move(170, 13)
        dif_l.move(170, 48)
        mul_l.move(170, 83)
        div_l.move(170, 118)


    def calculate(self):
        n1 = int(self.number_1.text())
        n2 = int(self.number_2.text())

        self.result_sum.display(n1 + n2)
        self.result_sub.display(n1 - n2)
        self.result_mul.display(n1 * n2)
        if n2 == 0:
            self.result_div.display('Error')
        else:
            self.result_div.display(round(n1 / n2, 3))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniCalculator()
    ex.show()
    sys.exit(app.exec())
