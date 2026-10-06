import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QCheckBox


class WidgetsHideNSeek(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 215, 105)
        self.setWindowTitle("Прятки для виджетов")

        self.checkbox1 = QCheckBox(self)
        self.checkbox1.setText("edit1")
        self.checkbox1.clicked.connect(self.checkbox_click)
        self.checkbox1.resize(80, 20)

        self.checkbox2 = QCheckBox(self)
        self.checkbox2.setText("edit2")
        self.checkbox2.clicked.connect(self.checkbox_click)
        self.checkbox2.resize(80, 20)

        self.checkbox3 = QCheckBox(self)
        self.checkbox3.setText("edit3")
        self.checkbox3.clicked.connect(self.checkbox_click)
        self.checkbox3.resize(80, 20)

        self.checkbox4 = QCheckBox(self)
        self.checkbox4.setText("edit4")
        self.checkbox4.clicked.connect(self.checkbox_click)
        self.checkbox4.resize(80, 20)

        self.checkbox1.move(5, 5)
        self.checkbox2.move(5, 30)
        self.checkbox3.move(5, 55)
        self.checkbox4.move(5, 80)

        self.checkbox1.setChecked(True)
        self.checkbox2.setChecked(True)
        self.checkbox3.setChecked(True)
        self.checkbox4.setChecked(True)

        self.edit1 = QLineEdit(self)
        self.edit1.setText('Поле edit1')
        self.edit1.resize(150, 20)
        self.edit1.move(60, 5)

        self.edit2 = QLineEdit(self)
        self.edit2.setText('Поле edit2')
        self.edit2.resize(150, 20)
        self.edit2.move(60, 30)

        self.edit3 = QLineEdit(self)
        self.edit3.setText('Поле edit3')
        self.edit3.resize(150, 20)
        self.edit3.move(60, 55)

        self.edit4 = QLineEdit(self)
        self.edit4.setText('Поле edit4')
        self.edit4.resize(150, 20)
        self.edit4.move(60, 80)

    def checkbox_click(self):
        self.edit1.hide()
        self.edit2.hide()
        self.edit3.hide()
        self.edit4.hide()

        if self.checkbox1.isChecked():
            self.edit1.show()
        if self.checkbox2.isChecked():
            self.edit2.show()
        if self.checkbox3.isChecked():
            self.edit3.show()
        if self.checkbox4.isChecked():
            self.edit4.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetsHideNSeek()
    ex.show()
    sys.exit(app.exec())
