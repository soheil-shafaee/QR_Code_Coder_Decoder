from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys

import qr_code_scanner as qr
import qr_history as qr_history


class ChooseContent(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()

        self.scanning: qr.QRScanner | None = None
        self.show_history: qr_history.HistoryPage | None = None


        # Define Widgets
        self.scan_page = self.findChild(QPushButton, "scan_button")
        self.close_button = self.findChild(QPushButton, "close_button")
        self.mini_button = self.findChild(QPushButton, "mini_button")

        # Do Action with our widgets
        self.scan_page.clicked.connect(self.go_to_scan)
        self.close_button.clicked.connect(self.close_win)
        self.mini_button.clicked.connect(self.mini_win)

    def load_ui(self) -> None:
        try:
            uic.loadUi("generate_first_page.ui", self)
            self.setFixedSize(423, 513)
            self.setWindowFlag(Qt.FramelessWindowHint)

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def go_to_scan(self):
        try:
            self.scanning = qr.QRScanner()
            self.scanning.show()
            self.close()
        except Exception as e:
            print(e)

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
