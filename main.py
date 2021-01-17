import function_UI
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    ui_display = function_UI.MainUI()
    ui_display.show()
    app.exec_()


if __name__ == "__main__":
    main()