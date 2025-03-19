from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
import sys


class EmailPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()


    def load_ui(self) -> None:
        try:
            uic.loadUi("email_page.ui", self)
        except Exception as e:
            print(e)
            sys.exit(1)


def main():
    try:
        app = QApplication(sys.argv)
        window_ui = EmailPage()
        window_ui.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
