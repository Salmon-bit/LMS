import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QRadioButton, QLabel)


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.button_grid: list[list[QPushButton]] = [[]]
        self.turn = 'X'
        self.map: list[list[str]] = [[]]

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("Крестики-нолики")

        self.x_radio = QRadioButton('X', self)
        self.o_radio = QRadioButton('O', self)
        self.x_radio.move(170, 20)
        self.o_radio.move(210, 20)
        self.x_radio.setChecked(True)
        self.x_radio.clicked.connect(self.radio_click)
        self.o_radio.clicked.connect(self.radio_click)


        for x in range(3):
            for y in range(3):
                pb = QPushButton(self)
                pb.clicked.connect(self.btn_click)
                pb.resize(50, 50)
                pb.move(125 + x * 50, 60 + y * 50)

                self.button_grid[x].append(pb)
            self.button_grid.append([])

        self.result = QLabel('Result', self)
        self.result.move(155, 250)

        self.new_game_button = QPushButton('Новая игра', self)
        self.new_game_button.move(155, 270)
        self.new_game_button.clicked.connect(self.restart_game)

    def btn_click(self):
        pass

    def restart_game(self):
        pass

    def radio_click(self):
        s = self.sender()
        self.turn = s.text()
        self.restart_game()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ttt = TicTacToe()
    ttt.show()
    sys.exit(app.exec())
