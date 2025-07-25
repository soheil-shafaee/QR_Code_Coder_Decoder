from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsBlurEffect, QLabel, QPushButton, QLineEdit, QMessageBox, \
    QColorDialog
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys

from verify.email_verify import email_checking
import qr_code_scanner as qr
import qr_history as his


class EmailPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()

        # Variable
        self.blur_effect: QGraphicsBlurEffect | None = None
        self.color: QColorDialog | None = None
        self.scan_page: qr.QRScanner | None = None
        self.history_page: his.HistoryPage | None = None

        # Define Widgets
        """Navbar"""
        self.close_button = self.findChild(QPushButton, "close_button")
        self.mini_button = self.findChild(QPushButton, "mini_button")

        """Main Body"""
        self.email_link = self.findChild(QLineEdit, "email_link")
        self.background_color_button = self.findChild(QPushButton, "background_colors")
        self.background_color_text = self.findChild(QLabel, "background_color_qr_code")
        self.qr_color_button = self.findChild(QPushButton, "QR_colors")
        self.qr_color_text = self.findChild(QLabel, "qr_color")
        self.generate_button = self.findChild(QPushButton, "generate_button")
        self.background_image = self.findChild(QLabel, "background_image")
        self.scan_button = self.findChild(QPushButton, "scan_button")
        self.history_button = self.findChild(QPushButton, "history_button")
        # Do Action with widgets
        """Navbar"""
        self.close_button.clicked.connect(self.close)
        self.mini_button.clicked.connect(self.showMinimized)

        """Main Body"""
        self.background_color_button.clicked.connect(self.change_background_color)
        self.generate_button.clicked.connect(self.generate_qr_code)
        self.scan_button.clicked.connect(self.return_scan)
        self.history_button.clicked.connect(self.go_histor)
        self.background_color_button.clicked.connect(self.change_background_color)

    def load_ui(self) -> None:
        try:
            uic.loadUi("email_page.ui", self)

            # Fix window size
            self.setFixedSize(423, 513)
            # Remove window navbar
            self.setWindowFlag(Qt.FramelessWindowHint)
            # Making Background Picture blur
            self.blur_effect = QGraphicsBlurEffect()
            self.blur_effect.setBlurRadius(15)
            self.background_image.setGraphicsEffect(self.blur_effect)

        except Exception as e:
            print(e)
            sys.exit(1)

    def change_background_color(self):
        self.color_tx = QColorDialog().getColor()
        try:
            self.background_color_text.setText(str(self.color_tx.name()))
            # self.background_color_text.setColor(self.color.name)
        except Exception as e:
            print(e)

    @email_checking
    def email_text_line(self):
        return self.email_link.text()

    def generate_qr_code(self):
        try:
            email_valid = self.email_text_line()
            if not email_valid:
                message = QMessageBox()
                message.setWindowTitle("Value Error")
                message.setIcon(QMessageBox.Warning)
                message.setText("Email Not Valid")
                message.exec_()
                return
            else:
                print(email_valid)
        except ValueError as e:
            print(e)


    def return_scan(self):
        """Going into scan page"""
        self.scan_page = qr.QRScanner()
        self.scan_page.show()
        self.close()

    def go_histor(self):
        """Going into History page"""
        self.history_page = his.HistoryPage()
        self.history_page.show()
        self.close()


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
