from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic
from pyzbar.pyzbar import decode
import sys
import cv2


class QRScanner(QMainWindow):
    """This class for using camera with OpenCv and then decode QR-Code and
    display into the Line Edit box"""
    def __init__(self):
        super(QRScanner, self).__init__()

        # Load UI file
        uic.loadUi("scanner.ui", self)

        # Finding Our Widgets
        self.scan_button = self.findChild(QPushButton, "scan_button")
        self.scan_screen = self.findChild(QLabel, "scanning_place")
        self.text_scan = self.findChild(QLineEdit, "text_scan")

        # Initialize Variables
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.camera_active = False

        # Using Scan button
        self.scan_button.clicked.connect(self.toggle_camera)
        self.timer.timeout.connect(self.update_frame)
        self.text_scan.setText("Your text scan!")



        # Display Scanner Window
        self.show()

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
        # This variable check camera turn on and take frame of that
        ret, frame = self.capture.read()

        if ret:
            # Camera is on ret = True, change the color of frame and decode it
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            decode_object = decode(frame)
            if decode_object:
                # decode object is list of the QR-Code information we need the first one data
                qr_data = decode_object[0].data.decode("utf-8")
                self.text_scan.setText(qr_data)
        # image variable change the format of the frame from the camera to can display in PyQt label
        image = QImage(rgb_frame.data, rgb_frame.shape[1], rgb_frame.shape[0], QImage.Format_RGB888)
        # Display camera into label
        self.scan_screen.setPixmap(QPixmap.fromImage(image))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QR_UI = QRScanner()
    app.exec_()
