from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
from qr_code_scanner import QRScanner
import sys


class WellcomePage(QMainWindow):
    """This Class displays wellcome window. By using start button you can
    start to use this app."""

    def __init__(self):
        super(WellcomePage, self).__init__()

        # Loading Wellcome Page UI
        uic.loadUi("wellcome_page.ui", self)

        # Finding Button
        self.start_button = self.findChild(QPushButton, "start_button")

        # Using button
        self.start_button.clicked.connect(self.let_start)

        # Define Variable for using scanner page
        self.scanner_page = None

        # Display Wellcome Page
        self.show()

    def let_start(self):
        self.scanner_page = QRScanner()
        self.scanner_page.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window_ui = WellcomePage()
    app.exec_()
