from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys

from verify.email_verify import email_checking

class EmailPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()


        # Define Widgets
        """Navbar"""
        self.close_button = self.findChild(QPushButton, "close_button")
        self.mini_button = self.findChild(QPushButton, "mini_button")

        """Main Body"""
        self.email_link = self.findChild(QLineEdit, "email_link")
        self.generate_button = self.findChild(QPushButton, "generate_button")
        # Do Action with widgets
        """Navbar"""
        self.close_button.clicked.connect(self.close)
        self.mini_button.clicked.connect(self.showMinimized)

        """Main Body"""
        self.generate_button.clicked.connect(self.generate_qr_code)


    def load_ui(self) -> None:
        try:
            uic.loadUi("email_page.ui", self)

            # Fix window size
            self.setFixedSize(423, 513)
            # Remove window navbar
            self.setWindowFlag(Qt.FramelessWindowHint)
        except Exception as e:
            print(e)
            sys.exit(1)

    @email_checking
    def email_text_line(self):
        return self.email_link.text()


    def generate_qr_code(self):
        try:
            print(self.email_text_line())
        except Exception as e:
            print(e)
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
