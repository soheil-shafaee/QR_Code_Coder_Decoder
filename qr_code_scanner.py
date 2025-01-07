from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import uic
import sys


class QRScanner(QMainWindow):
    def __init__(self):
        super(QRScanner, self).__init__()

        # Load UI file
        uic.loadUi("scanner.ui", self)

        # Display Scanner Window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QR_UI = QRScanner()
    app.exec_()
