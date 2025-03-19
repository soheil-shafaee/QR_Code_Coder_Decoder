from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys

import qr_code_scanner as qr
import qr_history as qr_history
from email_page import EmailPage


class ChooseContent(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()

        # Define Variables
        self.show_scanning: qr.QRScanner | None = None
        self.show_history: qr_history.HistoryPage | None = None
        self.show_email: EmailPage | None = None

        # Define Widgets
        """Top Navbar"""
        self.close_button = self.findChild(QPushButton, "close_button")
        self.mini_button = self.findChild(QPushButton, "mini_button")

        """Main Body"""
        self.email_button = self.findChild(QPushButton, "email_button")

        """Button Navbar"""
        self.scan_page = self.findChild(QPushButton, "scan_button")
        self.history_page = self.findChild(QPushButton, "history_button")

        # Do Action with our widgets
        """Top Navbar"""
        self.close_button.clicked.connect(self.close_win)
        self.mini_button.clicked.connect(self.mini_win)

        """Main Body"""
        self.email_button.clicked.connect(self.go_to_email_page)

        """Button Navbar"""
        self.scan_page.clicked.connect(self.go_to_scan)
        self.history_page.clicked.connect(self.go_to_history)

    def load_ui(self) -> None:
        try:
            uic.loadUi("generate_first_page.ui", self)
            self.setFixedSize(423, 513)
            self.setWindowFlag(Qt.FramelessWindowHint)

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def close_win(self) -> None:
        try:
            self.close()
        except Exception as e:
            print(e)

    def mini_win(self) -> None:
        self.showMinimized()

    def go_to_email_page(self) -> None:
        try:
            self.show_email = EmailPage()
            self.show_email.show()
            self.close()
        except Exception as e:
            print(e)

    def go_to_scan(self) -> None:
        try:
            self.show_scanning = qr.QRScanner()
            self.show_scanning.show()
            self.close()
        except Exception as e:
            print(e)

    def go_to_history(self) -> None:
        try:
            self.show_history = qr_history.HistoryPage()
            self.show_history.show()
            self.close()
        except Exception as e:
            print(e)


def main() -> None:
    app = QApplication(sys.argv)
    window_UI = ChooseContent()
    window_UI.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
