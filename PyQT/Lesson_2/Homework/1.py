from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore, QtWidgets
import sys


class Ui_MyNotes(object):
    def setupUi(self, MyNotes):
        MyNotes.setObjectName("MyNotes")
        MyNotes.resize(428, 328)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=MyNotes)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 401, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.contactName = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contactName.sizePolicy().hasHeightForWidth())
        self.contactName.setSizePolicy(sizePolicy)
        self.contactName.setObjectName("contactName")
        self.verticalLayout_4.addWidget(self.contactName)
        self.contactNumber = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contactNumber.sizePolicy().hasHeightForWidth())
        self.contactNumber.setSizePolicy(sizePolicy)
        self.contactNumber.setObjectName("contactNumber")
        self.verticalLayout_4.addWidget(self.contactNumber)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.addContactBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.addContactBtn.setObjectName("addContactBtn")
        self.horizontalLayout.addWidget(self.addContactBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.contactList = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contactList.sizePolicy().hasHeightForWidth())
        self.contactList.setSizePolicy(sizePolicy)
        self.contactList.setObjectName("contactList")
        self.verticalLayout_2.addWidget(self.contactList)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(MyNotes)
        QtCore.QMetaObject.connectSlotsByName(MyNotes)

    def retranslateUi(self, MyNotes):
        _translate = QtCore.QCoreApplication.translate
        MyNotes.setWindowTitle(_translate("MyNotes", "Записная книжка"))
        self.label_2.setText(_translate("MyNotes", "Имя"))
        self.label.setText(_translate("MyNotes", "Телефон"))
        self.addContactBtn.setText(_translate("MyNotes", "Добавить"))


class MyNotes(QWidget, Ui_MyNotes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_actions()

    def add_actions(self):
        self.addContactBtn.clicked.connect(self.add_contact)

    def add_contact(self):
        name = self.contactName.text()
        number = self.contactNumber.text()

        self.contactList.addItem(f"{name} {number}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_notes = MyNotes()
    my_notes.show()
    sys.exit(app.exec())
