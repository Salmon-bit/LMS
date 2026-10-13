from PySide6 import QtCore, QtWidgets
import sys
import datetime as dt


class SimplePlanner(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.retranslateUi()

        self.selected_date = dt.datetime.now().strftime('%Y-%m-%d')
        self.selected_time = '00:00:00'

    def setupUi(self):
        self.setGeometry(300, 300, 511, 412)
        self.setWindowTitle('Минипланировщик')

        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 511, 411))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.horizontalLayoutWidget)
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.timeChanged.connect(self.time_changed)
        self.verticalLayout.addWidget(self.timeEdit)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.horizontalLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.clicked.connect(self.calendar_clicked)
        self.verticalLayout.addWidget(self.calendarWidget)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.addEventBtn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.addEventBtn.setObjectName("addEventBtn")
        self.addEventBtn.clicked.connect(self.add_event)
        self.verticalLayout.addWidget(self.addEventBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.eventList = QtWidgets.QListWidget(parent=self.horizontalLayoutWidget)
        self.eventList.setObjectName("eventList")
        self.horizontalLayout.addWidget(self.eventList)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.addEventBtn.setText(_translate("Form", "Добавить событие"))

    def calendar_clicked(self, date):
        self.selected_date = date.toString('yyyy-MM-dd')

    def time_changed(self, time):
        self.selected_time = time.toString('HH:mm:ss')

    def add_event(self):
        add_text = f"{self.selected_date} {self.selected_time} - {self.lineEdit.text()}"
        self.eventList.addItem(add_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sp = SimplePlanner()
    sp.show()
    sys.exit(app.exec())
