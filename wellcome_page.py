from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import uic
import sys


class WellcomePage(QMainWindow):
    def __init__(self):
        super(WellcomePage, self).__init__()

        # Loading Wellcome Page UI
        uic.loadUi("wellcome_page.ui", self)

        # Display Wellcome Page
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window_ui = WellcomePage()
    app.exec_()