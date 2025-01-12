from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QMovie
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

        # Fixed Windows size
        self.setFixedSize(423, 494)

        # Finding our Widgets
        self.start_button = self.findChild(QPushButton, "start_button")
        self.gif_label = self.findChild(QLabel, "scan_gif")

        # Using button
        self.start_button.clicked.connect(self.let_start)

        # Play gif in QLabel
        self.movie = QMovie("images/QR.gif")
        self.gif_label.setMovie(self.movie)
        self.movie.start()

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
