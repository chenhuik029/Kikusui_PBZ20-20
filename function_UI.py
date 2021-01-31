from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QDesktopWidget
from PyQt5 import QtWidgets, QtCore, QtGui
from UIpy import Main_UI, CV_Console_UI, SEQ_Console_UI
from function_msgbox import msg_box_ok, msg_box_auto_close, msg_box_ok_cancel
from Instrument_PyVisa import Kikusui_PyVisa
from pyqt_led import Led
import sys
import re
import time
from threading import Thread


# Main UI
class MainUI(QMainWindow, Main_UI.Ui_MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.pushButton_Connect.setDisabled(True)
        # self.pushButton_CV_mode.setDisabled(True)
        # self.pushButton_Programmable_Mode.setDisabled(True)

        # Add a led Widget
        self.led_widget = Led(self, on_color=Led.green, off_color=Led.red, shape=Led.circle)
        self.led_widget.setFixedSize(25, 25)
        self.horizontalLayout_4.addWidget(self.led_widget)

        self.instrument = Kikusui_PyVisa.Kikusui_features()
        self.list_instrument = Kikusui_PyVisa.Kikusui_PyVisa()

        # Print out scanned equipment
        self.combobox_equipment_list()

        # Button connection
        self.actionExit.triggered.connect(self.close_app)
        self.pushButton_CV_mode.clicked.connect(self.goto_cv_console_mode)
        self.pushButton_Programmable_Mode.clicked.connect(self.goto_seq_console_mode)
        self.pushButton_refresh.clicked.connect(self.combobox_equipment_list)
        self.pushButton_Connect.clicked.connect(self.connect_equipment)
        self.comboBox_list_instrument.currentIndexChanged.connect(self.check_selected_equipment)


        # Variables
        self.equipment_list = []
        self.selected_equipment = ""
        self.active_session = False

    def close_app(self):
        msg_box_auto_close("Closing Program")
        self.close()

    # Switch to console mode
    def goto_cv_console_mode(self):
        self.close()
        self.console_mode = FV_Console_UI(self.selected_equipment)
        self.console_mode.show()

    def goto_seq_console_mode(self):
        self.close()
        self.seq_console_mode = Prog_Console_UI(self.selected_equipment)
        self.seq_console_mode.show()

    # Add connected equipment to the list
    def combobox_equipment_list(self):

        self.pushButton_Connect.setDisabled(True)
        self.pushButton_CV_mode.setDisabled(True)
        self.pushButton_Programmable_Mode.setDisabled(True)
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
        # self.equipment_list = self.list_instrument.list_connected_devices()
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
        status = True
        # status = self.instrument.connect_equipment(self.selected_equipment)
        if status is False:
            msg_box_ok(f'ERROR 001:\n\n{self.selected_equipment} is busy\n'
                       f'OR not available\n'
                       f'OR selection is incorrect!\n\n'
                       f'Please choose the correct equipment/ free up the equipment!')
        else:
            self.led_widget.turn_on()
            self.pushButton_CV_mode.setEnabled(True)
            self.pushButton_Programmable_Mode.setEnabled(True)


class FV_Console_UI(QMainWindow, CV_Console_UI.Ui_MainWindow):
    def __init__(self, selected_equipment):
        super().__init__()
        self.setupUi(self)

        self.read_thread = Thread(target=self.read_output)
        self.instrument = Kikusui_PyVisa.Kikusui_features()
        self.selected_equipment = selected_equipment

        # Sent event triggered
        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_ONOFF.clicked.connect(self.on_off_click)
        self.spinBox_OV.valueChanged.connect(self.adjust_output)
        self.doubleSpinBox_OV.valueChanged.connect(self.adjust_output)

        # Add a LED Widget
        self.led_widget = Led(self, on_color=Led.green, off_color=Led.red, shape=Led.circle)
        self.led_widget.setFixedSize(25, 25)
        self.horizontalLayout_6.addWidget(self.led_widget)

        # Add combo box list
        self.comboBox.addItems(["UNIPolar", "BIPolar"])
        self.comboBox.setCurrentIndex(0)

        # Define add variables
        self.polarity = ""
        self.set_OV_int = ""
        self.set_OV_dec = ""
        self.set_OV_lim_int = ""
        self.set_OV_lim_dec = ""
        self.set_cur_lim_int = ""
        self.set_cur_lim_dec = ""
        self.vout_read = 0
        self.iout_read = 0
        self.status_on_off = False
        self.read_output_stat = False

    def close_app(self):
        # close thread for read output voltage
        self.read_output_stat = False
        self.instrument.on_off_equipment(0)
        self.instrument.disconnect_equipment()
        msg_box_auto_close("Closing Program")
        self.close()

    def navigate_back(self):
        # close thread for read output voltage
        self.read_output_stat = False
        self.instrument.on_off_equipment(0)
        self.instrument.disconnect_equipment()
        self.close()
        self.main_ui = MainUI()
        self.main_ui.show()

    def on_off_click(self):

        # Turn ON
        if not self.status_on_off:

            self.read_user_input()
            # self.read_thread = Thread(target=self.read_output)

            # Check output is > limit set
            if self.set_output_vol >= self.set_output_vol_limit:
                msg_box_ok("Error 002:\n"
                           "Output Voltage Limit must be larger than set Output Voltage!")

            else:
                # Turn On output of the Equipment
                self.instrument.connect_equipment(self.selected_equipment)
                status_set_voltage = self.instrument.set_unipolar_cv_output("CV", self.polarity, self.set_output_vol, self.set_output_vol_limit, self.set_cur_limit)
                status_on_output = self.instrument.on_off_equipment(1)

                if status_on_output and status_set_voltage:
                    # Disable control
                    self.comboBox.setDisabled(True)
                    self.spinBox_OV_Lim.setDisabled(True)
                    self.doubleSpinBox_OV_Lim.setDisabled(True)
                    self.spinBox_Cur_Lim.setDisabled(True)
                    self.doubleSpinBox_Cur_lim.setDisabled(True)
                    self.spinBox_OV.setMaximum(int(self.set_OV_lim_int) - 1)
                    self.spinBox_OV.setMinimum(-(int(self.set_OV_lim_int) - 1))
                    self.led_widget.turn_on()
                    self.status_on_off = True

                    # Enable read output and display
                    self.read_thread = Thread(target=self.read_output)
                    self.read_output_stat = True
                    self.read_thread.start()

                else:
                    msg_box_ok("Error 003:\n"
                               "Unable to communicate with equipment.\n"
                               "Failed to turn on the output.\n"
                               "Please return to previous page to reconnect the equipment")
        # Turn OFF
        else:
            # Enable control
            self.comboBox.setDisabled(False)
            self.spinBox_OV_Lim.setDisabled(False)
            self.doubleSpinBox_OV_Lim.setDisabled(False)
            self.spinBox_Cur_Lim.setDisabled(False)
            self.doubleSpinBox_Cur_lim.setDisabled(False)
            self.spinBox_OV.setMaximum(20)
            self.spinBox_OV.setMinimum(-20)
            self.read_output_stat = False

            # Turn off the equipment
            self.led_widget.turn_off()
            self.instrument.on_off_equipment(0)
            self.status_on_off = False
            self.read_thread.join()

    def adjust_output(self):
        if self.status_on_off:
            self.read_user_input()
            self.instrument.update_output_voltage(self.set_output_vol)

    def read_output(self):
        while self.read_output_stat:
            self.vout_read = self.instrument.read_output_supply()[0]
            self.iout_read = self.instrument.read_output_supply()[1]
            self.lcdNumber_Voltage.display(f'{self.vout_read}')
            self.lcdNumber_Current.display(f'{self.iout_read}')
            # time.sleep(0.3)

    def read_user_input(self):
        self.polarity = self.comboBox.currentText()
        self.set_OV_int = self.spinBox_OV.text()
        self.set_OV_dec = self.doubleSpinBox_OV.text()
        self.set_OV_lim_int = self.spinBox_OV_Lim.text()
        self.set_OV_lim_dec = self.doubleSpinBox_OV_Lim.text()
        self.set_cur_lim_int = self.spinBox_Cur_Lim.text()
        self.set_cur_lim_dec = self.doubleSpinBox_Cur_lim.text()

        self.set_output_vol = int(self.set_OV_int) + float(self.set_OV_dec)
        self.set_output_vol_limit = int(self.set_OV_lim_int) + float(self.set_OV_lim_dec)
        self.set_cur_limit = int(self.set_cur_lim_int) + float(self.set_cur_lim_dec)


class Prog_Console_UI(QMainWindow, SEQ_Console_UI.Ui_MainWindow):
    def __init__(self, selected_equipment):
        super().__init__()
        self.setupUi(self)

        # Move to centre of screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.tableWidget.setColumnWidth(0, 170)

        # Add item to combo box
        self.comboBox_polarity.addItems(["UNIPolar", "BIPolar"])
        self.comboBox_mode.addItems(["CV", "CC"])
        self.comboBox_polarity.setCurrentIndex(0)
        self.comboBox_mode.setCurrentIndex(0)

        # Sent event triggered
        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_Back.clicked.connect(self.navigate_back)
        self.pushButton_CreateTable.clicked.connect(self.create_table)
        self.pushButton_ClearTable.clicked.connect(self.clear_table)


        # Define Variable
        self.selected_equipment = selected_equipment
        self.table_created = False
        self.steps = 0

    def close_app(self):
        self.close()

    def navigate_back(self):
        # close thread for read output voltage
        self.close()
        self.main_ui = MainUI()
        self.main_ui.show()

    def create_table(self):
        self.steps = int(self.spinBox_steps.text())
        exist_step = self.tableWidget.columnCount() - 1

        for step in range(self.steps):
            column_to_add = exist_step + (step + 1)
            self.tableWidget.insertColumn(column_to_add)
            self.tableWidget.setHorizontalHeaderItem(column_to_add, QtWidgets.QTableWidgetItem(str(column_to_add)))

    def clear_table(self):
        exist_step = self.tableWidget.columnCount()
        for step in range(exist_step):
            self.tableWidget.removeColumn(1)


