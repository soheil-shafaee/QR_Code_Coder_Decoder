from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QGraphicsEffect, \
    QGraphicsBlurEffect
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic
from pyzbar.pyzbar import decode
import sys
import cv2
import pymysql

from qr_history import HistoryPage
from choose_content_page import ChooseContent

con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="qr_code"
)
cur = con.cursor()


class QRScanner(QMainWindow):
    """This class for using camera with OpenCv and then decode QR-Code and
    display into the Line Edit box"""

    def __init__(self):
        try:
            super(QRScanner, self).__init__()

            self.qr_detected = False

            self.history: HistoryPage | None = None
            self.choose_page: ChooseContent | None = None

            # Load UI file
            uic.loadUi("scanner.ui", self)
            self.setFixedSize(423, 513)
            self.setWindowFlag(Qt.FramelessWindowHint)

            # Define Widgets in form
            self.scan_button = self.findChild(QPushButton, "scan_button")
            self.go_choose = self.findChild(QPushButton, "generate_button")
            self.history_button = self.findChild(QPushButton, "history_button")
            # Define Widgets in main body
            self.scan_screen = self.findChild(QLabel, "scanning_place")
            self.text_scan = self.findChild(QLineEdit, "text_scan")
            self.image_back = self.findChild(QLabel, "background_image")
            # Navbar Widgets
            self.close_window = self.findChild(QPushButton, "close_button")
            self.minimize_window = self.findChild(QPushButton, "mini_button")
            # Set Enabled for set Text
            self.text_scan.setEnabled(False)

            # Blur Effect
            self.blur_effect = QGraphicsBlurEffect()
            self.blur_effect.setBlurRadius(15)
            self.image_back.setGraphicsEffect(self.blur_effect)

            # Initialize Variables
            self.capture = cv2.VideoCapture(0)
            self.timer = QTimer()
            self.camera_active = False

            # Using Scan button
            self.scan_button.clicked.connect(self.toggle_camera)
            self.timer.timeout.connect(self.update_frame)
            # self.text_scan.setText("Your text scan!")
            self.close_window.clicked.connect(self.close_win)
            self.minimize_window.clicked.connect(self.mini_win)

            # Using History button
            self.history_button.clicked.connect(self.go_to_history_page)

            # Using Scanner button
            self.go_choose.clicked.connect(self.go_to_choose_page)

            # Display Scanner Window
            self.show()
        except Exception as e:
            print(e)

    def toggle_camera(self):
        """This function, for turn on to the camera and
        then after that releasing video."""
        if not self.camera_active:
            self.camera_active = True
            self.timer.start(30)
        else:
            self.camera_active = False
            self.timer.stop()
            self.scan_screen.clear()
            self.capture.release()

    def update_frame(self):
        """This function, update frame of the camera and
         then display camera into the label then by using decode module from
         pyzbar library decoding QR-Code"""

        if self.qr_detected:
            return
        # This variable check camera turn on and take frame of that
        ret, frame = self.capture.read()

        if ret:
            # Camera is on ret = True, change the color of frame and decode it
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            decode_object = decode(frame)
            if decode_object:
                # decode object is list of the QR-Code information we need the first one data
                qr_data = decode_object[0].data.decode("utf-8")
                self.text_scan.setEnabled(True)
                self.text_scan.setText(qr_data)
                com = """INSERT INTO qr_code_logs(Address, Type, DateTime) VALUES(%s, %s, NOW())"""
                try:
                    cur.execute(com, (qr_data, "SCAN"))
                    con.commit()
                except Exception as e:
                    print(e)
                    con.rollback()

                # Stop Timer and turn off Camera
                self.qr_detected = True
                self.timer.stop()
                self.capture.release()
                self.scan_screen.clear()

        # image variable change the format of the frame from the camera to can display in PyQt label
        image = QImage(rgb_frame.data, rgb_frame.shape[1], rgb_frame.shape[0], QImage.Format_RGB888)
        # Display camera into label
        self.scan_screen.setPixmap(QPixmap.fromImage(image))

    def go_to_history_page(self):
        self.history = HistoryPage()
        self.history.show()
        self.close()

    def go_to_choose_page(self):
        self.choose_page = ChooseContent()
        self.choose_page.show()
        self.close()

    def close_win(self):
        self.close()

    def mini_win(self):
        self.showMinimized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QR_UI = QRScanner()
    app.exec_()
