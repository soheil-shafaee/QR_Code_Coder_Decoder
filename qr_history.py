from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys
import pymysql

import qr_code_scanner as qr

con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="qr_code"
)

cur = con.cursor()
com = """SELECT Address, DateTime FROM qr_code_logs ORDER BY  DateTime DESC"""



class HistoryPage(QMainWindow):
    def __init__(self):
        super(HistoryPage, self).__init__()

        # Loading UI file
        uic.loadUi("qr_history.ui", self)

        # Fixed Window size and Window flag
        self.setFixedSize(423, 513)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.qr_list = []

        # Define Widgets
        self.scan_button = self.findChild(QPushButton, "scan_button")

        # Define label for QR Code Address and Date time and Delete button
        self.address_label = self.findChild(QLabel, "qr_address")
        self.datetime_label = self.findChild(QLabel, "date_time")
        self.address_label2 = self.findChild(QLabel, "qr_address_2")
        self.datetime_label2 = self.findChild(QLabel, "date_time_2")
        self.address_label3 = self.findChild(QLabel, "qr_address_3")
        self.datetime_label3 = self.findChild(QLabel, "date_time_3")
        self.address_label4 = self.findChild(QLabel, "qr_address_4")
        self.datetime_label4 = self.findChild(QLabel, "date_time_4")


        self.close_button = self.findChild(QPushButton, "close_button")
        self.minimize_button = self.findChild(QPushButton, "mini_button")

        cur.execute(com)
        result = cur.fetchall()
        for address, date in result:
            date_format = date.strftime("%d %b %Y, %H:%m %p")
            self.qr_list.append([address, date_format])
            self.number = len(self.qr_list)
            if self.number == 4:
                break
        if self.number < 4:
            j = 4 - self.number
            for i in range(j):
                self.qr_list.append(["There's not QR Code Address", "      There is no date"])

        try:
            self.address_label.setText(str(self.qr_list[0][0]))
            self.datetime_label.setText(str(self.qr_list[0][1]))
            self.address_label2.setText(str(self.qr_list[1][0]))
            self.datetime_label2.setText(str(self.qr_list[1][1]))
            self.address_label3.setText(str(self.qr_list[2][0]))
            self.datetime_label3.setText(str(self.qr_list[2][1]))
            self.address_label4.setText(str(self.qr_list[3][0]))
            self.datetime_label4.setText(str(self.qr_list[3][1]))
        except Exception as e:
            print(e)


        # Make Action with Widgets
        self.close_button.clicked.connect(self.close_window)
        self.minimize_button.clicked.connect(self.mini_window)
        self.scan_button.clicked.connect(self.back_to_scan)

        # Display UI
        self.show()

    # Close window with custom button
    def close_window(self):
        self.close()

    # Minimize window with custom button
    def mini_window(self):
        self.showMinimized()

    # Back to the scan page
    def back_to_scan(self):
        self.scan = qr.QRScanner()
        self.scan.show()
        self.close()

    # Delete Data from database and qr_list
    def delete_data(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_history = HistoryPage()
    app.exec_()
