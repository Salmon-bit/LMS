from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap, QColor, QImage, QTransform
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(403, 387)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.channelButtons = QtWidgets.QButtonGroup(Form)
        self.channelButtons.setObjectName("channelButtons")
        self.channelButtons.addButton(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.channelButtons.addButton(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.channelButtons.addButton(self.pushButton_5)
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.channelButtons.addButton(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.rotateButtons = QtWidgets.QButtonGroup(Form)
        self.rotateButtons.setObjectName("rotateButtons")
        self.rotateButtons.addButton(self.pushButton)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.rotateButtons.addButton(self.pushButton_2)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PIL 2.0"))
        self.pushButton_3.setText(_translate("Form", "R"))
        self.pushButton_4.setText(_translate("Form", "G"))
        self.pushButton_5.setText(_translate("Form", "B"))
        self.pushButton_6.setText(_translate("Form", "All"))
        self.pushButton.setText(_translate("Form", "Против часовой стрелки"))
        self.pushButton_2.setText(_translate("Form", "По часовой стрелке"))


class MyPillow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.fname, _ = QFileDialog.getOpenFileName(
            self,
            'Выбрать изображение',
            '',
            'JPG-Изображение (*.jpg);;PNG-Изображение (*.png);;Все файлы (*)'
        )

        self.curr_image = QImage(self.fname)

        self.setupUi(self)
        self.label.setPixmap(QPixmap.fromImage(self.curr_image))

        self.connect_buttons()

    def keep_channels(self, image: QImage, keep: list[str] = ['r']):
        result = image

        for y in range(result.height()):
            for x in range(result.width()):
                color = result.pixelColor(x, y)
                result.setPixelColor(
                    x, y,
                    QColor(
                        color.red()   if "r" in keep else 0,
                        color.green() if "g" in keep else 0,
                        color.blue()  if "b" in keep else 0,
                    )
                )

        return result

    def connect_buttons(self):
        self.pushButton_3.clicked.connect(self.color_button_pressed)
        self.pushButton_4.clicked.connect(self.color_button_pressed)
        self.pushButton_5.clicked.connect(self.color_button_pressed)
        self.pushButton_6.clicked.connect(self.color_button_pressed)

        self.pushButton.clicked.connect(self.rotate_button_pressed)
        self.pushButton_2.clicked.connect(self.rotate_button_pressed)

    def color_button_pressed(self):
        s = self.sender()

        match s.text().lower():
            case 'r' | 'g' | 'b':
                self.curr_image = self.keep_channels(QImage(self.fname), s.text().lower())
                self.label.setPixmap(QPixmap.fromImage(self.curr_image))
            case _:
                self.curr_image = QImage(self.fname)
                self.label.setPixmap(QPixmap.fromImage(self.curr_image))

    def rotate_button_pressed(self):
        s = self.sender()

        match s.text().lower():
            case 'против часовой стрелки':
                pm = QPixmap.fromImage(self.curr_image).transformed(QTransform().rotate(-90))
                self.curr_image = pm.toImage()
                self.label.setPixmap(pm)
            case _:
                pm = QPixmap.fromImage(self.curr_image).transformed(QTransform().rotate(90))
                self.curr_image = pm.toImage()
                self.label.setPixmap(pm)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mp = MyPillow()
    mp.show()
    sys.exit(app.exec())
