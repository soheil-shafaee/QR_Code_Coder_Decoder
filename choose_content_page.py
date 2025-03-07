from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic
import sys


class ChooseContent(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()

    def load_ui(self) -> None:
        try:
            self.setFixedSize(423, 513)
            uic.loadUi("generate_first_page.ui", self)

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


def main() -> None:
    app = QApplication(sys.argv)
    window_UI = ChooseContent()
    window_UI.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
