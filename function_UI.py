from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
from UIpy import Main_UI, CV_Console_UI
from function_msgbox import msg_box_ok, msg_box_auto_close, msg_box_ok_cancel
import sys


# Main UI
class MainUI(QMainWindow, Main_UI.Ui_MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.console_mode = Console_UI()
        self.combobox_equipment_list()
        self.actionExit.triggered.connect(self.close_app)
        self.pushButton_CV_mode.clicked.connect(self.goto_cv_console_mode)

    def close_app(self):
        msg_box_auto_close("Closing Program")
        self.close()

    def goto_cv_console_mode(self):
        self.close()
        self.console_mode.show()

    def combobox_equipment_list(self):
        if self.comboBox_list_instrument.currentIndex() < 0:
            self.comboBox_list_instrument.addItem("Please select the targetted instrument to connect ...")
            self.comboBox_list_instrument.setCurrentIndex(0)
        else:
            self.comboBox_list_instrument.addItems(["Testing", "Testing 2"])

    def scan_equipment_list(self):
        pass


class Console_UI(QMainWindow, CV_Console_UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_ONOFF.clicked.connect(self.on_off_click)

    def close_app(self):
        msg_box_auto_close("Closing Program")
        self.close()

    def navigate_back(self):
        self.close()
        self.main_ui = MainUI()
        self.main_ui.equipment_list_address()
        self.main_ui.show()

    def on_off_click(self):
        pass

