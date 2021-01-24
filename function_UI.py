from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
from UIpy import Main_UI, CV_Console_UI
from function_msgbox import msg_box_ok, msg_box_auto_close, msg_box_ok_cancel
from Instrument_PyVisa import Kikusui_PyVisa
from pyqt_led import Led
import sys
import re
import time


# Main UI
class MainUI(QMainWindow, Main_UI.Ui_MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_Connect.setDisabled(True)
        self.pushButton_CV_mode.setDisabled(True)
        self.pushButton_Programmable_Mode.setDisabled(True)

        # Add a led Widget
        self.led_widget = Led(self, on_color=Led.green, off_color=Led.red, shape=Led.circle)
        self.led_widget.setFixedSize(25, 25)
        self.horizontalLayout_4.addWidget(self.led_widget)

        self.console_mode = Console_UI()
        self.pyvisa = Kikusui_PyVisa.Kikusui_PyVisa()

        # Print out scanned equipment
        self.combobox_equipment_list()

        # Button connection
        self.actionExit.triggered.connect(self.close_app)
        self.pushButton_CV_mode.clicked.connect(self.goto_cv_console_mode)
        self.pushButton_refresh.clicked.connect(self.combobox_equipment_list)
        self.pushButton_Connect.clicked.connect(self.connect_equipment)
        self.comboBox_list_instrument.currentIndexChanged.connect(self.check_selected_equipment)

        # Variables
        self.equipment_list = []
        self.selected_equipment = ""

    def close_app(self):
        msg_box_auto_close("Closing Program")
        self.close()

    # Switch to console mode
    def goto_cv_console_mode(self):
        self.close()
        self.console_mode.show()

    # Add connected equipment to the list
    def combobox_equipment_list(self):
        self.comboBox_list_instrument.clear()
        self.scan_equipment_list()
        self.led_widget.turn_off()

        if self.comboBox_list_instrument.currentIndex() < 0:
            self.comboBox_list_instrument.addItem("Please select the targetted instrument to connect ...")
            self.comboBox_list_instrument.setCurrentIndex(0)

        for equipment in self.equipment_list:
            # To filter out non-USB connection
            pattern = re.compile("USB[0-9]")
            if pattern.match(equipment.split("::", 4)[0]):
                # Filter out non Kikusui PBZ20-20 equipment
                if equipment.split("::", 4)[1] == "0x0B3E" and equipment.split("::", 4)[2] == "0x1012":
                    self.comboBox_list_instrument.addItem(equipment)

    # Scan connected equipment
    def scan_equipment_list(self):
        # self.equipment_list = self.basic_pyvisa.list_connected_devices()

        # To be deleted when actual instrument was used.
        self.equipment_list = ('USB0::0x0B3E::0x1012::XF001773::0::INSTR', 'ASRL4::INSTR', 'ASRL8::INSTR')

    # Check selected equipment
    def check_selected_equipment(self):
        if self.comboBox_list_instrument.currentIndex() > 0:
            self.selected_equipment = self.comboBox_list_instrument.currentText()
            self.pushButton_Connect.setEnabled(True)
        else:
            self.selected_equipment = ""
            self.pushButton_Connect.setDisabled(True)

    # Connect to selected equipment
    def connect_equipment(self):
        self.selected_equipment = self.comboBox_list_instrument.currentText()
        status = self.pyvisa.connect_device(self.selected_equipment)
        if status is False:
            msg_box_ok(f'ERROR 001:\n\n{self.selected_equipment} is busy\n'
                       f'OR not available\n'
                       f'OR selection is incorrect!\n\n'
                       f'Please choose the correct equipment/ free up the equipment!')
        else:
            self.led_widget.turn_on()
            self.pushButton_CV_mode.setEnabled(True)
            self.pushButton_Programmable_Mode.setEnabled(True)


class Console_UI(QMainWindow, CV_Console_UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_ONOFF.clicked.connect(self.on_off_click)

        # Add a led Widget
        self.led_widget = Led(self, on_color=Led.green, off_color=Led.red, shape=Led.circle)
        self.led_widget.setFixedSize(25, 25)
        self.horizontalLayout_6.addWidget(self.led_widget)

        self.set_OV_int = ""
        self.set_OV_dec = ""
        self.set_OV_lim_int = ""
        self.set_OV_lim_dec = ""
        self.set_cur_lim_int = ""
        self.set_cur_lim_dec = ""
        self.status_on_off = False

    def close_app(self):
        msg_box_auto_close("Closing Program")
        self.close()

    def navigate_back(self):
        self.close()
        self.main_ui = MainUI()
        self.main_ui.show()

    def on_off_click(self):

        # Turn ON
        if not self.status_on_off:
            self.set_OV_int = self.spinBox_OV.text()
            self.set_OV_dec = self.doubleSpinBox_OV.text()
            self.set_OV_lim_int = self.spinBox_OV_Lim.text()
            self.set_OV_lim_dec = self.doubleSpinBox_OV_Lim.text()
            self.set_cur_lim_int = self.spinBox_Cur_Lim.text()
            self.set_cur_lim_dec = self.doubleSpinBox_Cur_lim.text()

            self.set_output_vol = int(self.set_OV_int) + float(self.set_OV_dec)
            self.set_output_vol_limit = int(self.set_OV_lim_int) + float(self.set_OV_lim_dec)
            self.set_cur_limit = int(self.set_cur_lim_int) + float(self.set_cur_lim_dec)

            if self.set_output_vol >= self.set_output_vol_limit:
                msg_box_ok("Error 002:\n"
                           "Output Voltage Limit must be larger than set Output Voltage!")

            else:
                self.led_widget.turn_on()
                self.status_on_off = True
                self.spinBox_OV_Lim.setDisabled(True)
                self.doubleSpinBox_OV_Lim.setDisabled(True)
                self.spinBox_Cur_Lim.setDisabled(True)
                self.doubleSpinBox_Cur_lim.setDisabled(True)
                self.lcdNumber_Voltage.display(f'{self.set_output_vol}')

        # Turn OFF
        else:
            self.led_widget.turn_off()
            self.spinBox_OV_Lim.setDisabled(False)
            self.doubleSpinBox_OV_Lim.setDisabled(False)
            self.spinBox_Cur_Lim.setDisabled(False)
            self.doubleSpinBox_Cur_lim.setDisabled(False)
            self.status_on_off = False


