from PySide6.QtWidgets import (QWidget, QApplication, QCheckBox, QPlainTextEdit, QPushButton)
import sys


class MacOrder(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.menu_checkboxes: list[QCheckBox] = []
        self.positions: list[str] = ["Чизбургер", "Гамбургер", "Кока-кола", "Наггетсы"]

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 450)
        self.setWindowTitle("Заказ в Макдональдс")

        for p in self.positions:
            chb = QCheckBox(self)
            chb.setText(p)
            self.menu_checkboxes.append(chb)

        for i in range(len(self.menu_checkboxes)):
            self.menu_checkboxes[i].move(5, 20 * i + 5)

        self.order_btn = QPushButton('Заказать', self)
        self.order_btn.resize(80, 25)
        self.order_btn.move(5, 20 * len(self.menu_checkboxes) + 15)
        self.order_btn.clicked.connect(self.order_func)

        self.result = QPlainTextEdit(self)
        self.result.resize(290, 250)
        self.result.move(5, 20 * len(self.menu_checkboxes) + 45)
        self.result.setDisabled(True)

    def order_func(self):
        output = "Ваш заказ:\n\n"

        for cb in self.menu_checkboxes:
            if cb.isChecked():
                output += f"{self.positions[self.menu_checkboxes.index(cb)]}"
                output += "\n"

        self.result.setPlainText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MacOrder()
    win.show()
    sys.exit(app.exec())
