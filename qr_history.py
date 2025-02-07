from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys


class HistoryPage(QMainWindow):
    def __init__(self):
        super(HistoryPage, self).__init__()

        # Loading UI file
        uic.loadUi("qr_history.ui", self)

        # Fixed Window size and Window flag
        self.setFixedSize(423, 513)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Define Widgets
        self.close_button = self.findChild(QPushButton, "close_button")
        self.minimize_button = self.findChild(QPushButton, "mini_button")

        # Make Action with Widgets
        self.close_button.clicked.connect(self.close_window)
        self.minimize_button.clicked.connect(self.mini_window)

        # Display UI
        self.show()

    # Close window with custom button
    def close_window(self):
        self.close()

    # Minimize window with custom button
    def mini_window(self):
        self.showMinimized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_history = HistoryPage()
    app.exec_()
