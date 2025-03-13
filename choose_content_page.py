from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys


class ChooseContent(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()


        self.close_button = self.findChild(QPushButton, "close_button")
        self.mini_button = self.findChild(QPushButton, "mini_button")




    def load_ui(self) -> None:
        try:
            uic.loadUi("generate_first_page.ui", self)
            self.setFixedSize(423, 513)
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.close_button.clicked.connect(self.close_win)
            self.mini_button.clicked.connect(self.mini_win)

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def close_win(self):
        try:
            self.close()
        except Exception as e:
            print(e)

    def mini_win(self):
        self.showMinimized()


def main() -> None:
    app = QApplication(sys.argv)
    window_UI = ChooseContent()
    window_UI.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
