from PyQt6.QtWidgets import (QLineEdit, QWidget, QApplication, QCheckBox, 
                             QPlainTextEdit, QPushButton)
import sys


class MyWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.prices = {
            "Чизбургер": 10,
            "Гамбургер": 20,
            "Кока-кола": 15,
            "Наггетсы": 30
        }
        self.checkboxes: list[QCheckBox] = []
        self.inputs: list[QLineEdit] = []
        self.positions: list[str] = ["Чизбургер", "Гамбургер", "Кока-кола", "Наггетсы"]

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 450)
        self.setWindowTitle("Заказ в Макдональдс 2")
        
        for p in self.positions:
            chb = QCheckBox(self)
            chb.setText(p)
            chb.clicked.connect(self.add_position)
            self.checkboxes.append(chb)

            le = QLineEdit(self)
            le.setText('0')
            le.setDisabled(True)
            self.inputs.append(le)

        for i in range(len(self.checkboxes)):
            self.checkboxes[i].move(5, 20 * i + 5)
            self.inputs[i].resize(40, 20)
            self.inputs[i].move(150, 20 * i + 5)

        self.orderButton = QPushButton('Заказать', self)
        self.orderButton.resize(80, 25)
        self.orderButton.move(5, 20 * len(self.checkboxes) + 15)
        self.orderButton.clicked.connect(self.order_func)

        self.order = QPlainTextEdit(self)
        self.order.resize(290, 250)
        self.order.move(5, 20 * len(self.checkboxes) + 45)
        self.order.setDisabled(True)

    def add_position(self):
        sender_text: str = self.sender().text()
        position_index = self.positions.index(sender_text)
        if self.sender().isChecked():
            self.inputs[position_index].setDisabled(False)
            self.inputs[position_index].setText('1')
        else:
            self.inputs[position_index].setDisabled(True)
            self.inputs[position_index].setText('0')

    def order_func(self):
        output = "Ваш заказ\n\n"
        total_price = 0

        for i in self.inputs:
            if i.text() != '0':
                current_price = int(i.text()) * self.prices.get(self.positions[self.inputs.index(i)])
                output += f"{self.positions[self.inputs.index(i)]}{'-' * 5}{i.text()}{'-' * 5}{current_price}"
                total_price += current_price
                output += "\n"

        output += f"\nИтого: {total_price}"
        self.order.setPlainText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec())
