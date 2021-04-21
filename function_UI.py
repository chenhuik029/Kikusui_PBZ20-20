from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QDesktopWidget
from PyQt5 import QtWidgets, QtCore, QtGui
from UIpy import Main_UI, CV_Console_UI, SEQ_Console_UI, SEQ_AddEdit_UI
from function_msgbox import msg_box_ok, msg_box_auto_close, msg_box_ok_cancel, about_show
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
        self.actionAbout.triggered.connect(self.about)

        # Variables
        self.equipment_list = []
        self.selected_equipment = ""
        self.active_session = False

    def about(self):
        about_show()

    def close_app(self):
        msg_box_auto_close("Closing Program")
        self.close()

    # Switch to constant voltage console mode
    def goto_cv_console_mode(self):
        self.close()
        self.console_mode = FV_Console_UI(self.selected_equipment)
        self.console_mode.show()

    # Switch to sequential console mode
    def goto_seq_console_mode(self):
        self.close()
        self.seq_console_mode = Set_Prog_Console_UI(self.selected_equipment)
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
        self.equipment_list = self.list_instrument.list_connected_devices()
        # To be deleted when actual instrument was used.
        # self.equipment_list = ('USB0::0x0B3E::0x1012::XF001773::0::INSTR', 'ASRL4::INSTR', 'ASRL8::INSTR')

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
        status = self.instrument.connect_equipment(self.selected_equipment)
        # status = True

        if status is False:
            msg_box_ok(f'ERROR 001:\n\n{self.selected_equipment} is busy\n'
                       f'OR not available\n'
                       f'OR selection is incorrect!\n\n'
                       f'Please choose the correct equipment/ free up the equipment!')
        else:
            self.led_widget.turn_on()
            self.pushButton_CV_mode.setEnabled(True)
            self.pushButton_Programmable_Mode.setEnabled(True)


# Fixed Voltage UI
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
                status_set_voltage = self.instrument.set_cv_output("CV", self.polarity, self.set_output_vol,
                                                                   self.set_output_vol_limit,
                                                                   self.set_cur_limit)
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


# Sequential Voltage UI
class Set_Prog_Console_UI(QMainWindow, SEQ_Console_UI.Ui_MainWindow):
    def __init__(self, selected_equipment):
        super().__init__()
        self.setupUi(self)
        self.read_thread = Thread(target=self.read_output)
        self.pushButton_StoreSequency.setDisabled(True)
        self.pushButton_AddEditSeq.setDisabled(True)
        self.pushButton_DelStep.setDisabled(True)
        self.instrument = Kikusui_PyVisa.Kikusui_features()

        # Move UI to centre of screen
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
        self.pushButton_AddSteps.clicked.connect(self.create_table)
        self.pushButton_ClearSteps.clicked.connect(self.clear_table)
        self.tableWidget.doubleClicked.connect(self.add_edit_step)
        self.pushButton_AddEditSeq.clicked.connect(self.add_edit_step)
        self.pushButton_DelStep.clicked.connect(self.delete_step)
        self.pushButton_StoreSequency.clicked.connect(self.store_sequence)
        self.pushButton_RunSequence.clicked.connect(self.run_sequence)

        # Define Variable
        self.read_output_stat = False
        self.selected_equipment = selected_equipment
        self.table_created = False
        self.steps = 0
        self.step_selected = 0
        self.columnCount = 0
        self.rowCount = self.tableWidget.rowCount()

    def close_app(self):
        self.close()

    def navigate_back(self):
        # close thread for read output voltage
        status = msg_box_ok_cancel("Please store the sequence settings before navigate to previous page.\n\n"
                                   "Press 'Cancel' to cancel the BACK action and proceed to 'Store Sequence'.\n"
                                   "Press 'OK' to exit the EDIT mode.")
        if status:
            self.close()
            self.main_ui = MainUI()
            self.main_ui.show()

    def create_table(self):
        self.steps = int(self.spinBox_steps.text())

        if int(self.steps) > 0:
            self.pushButton_StoreSequency.setDisabled(False)
            self.pushButton_AddEditSeq.setDisabled(False)
            self.pushButton_DelStep.setDisabled(False)

            exist_step = self.tableWidget.columnCount() - 1

            for step in range(self.steps):
                column_to_add = exist_step + (step + 1)
                self.tableWidget.insertColumn(column_to_add)
                self.tableWidget.setHorizontalHeaderItem(column_to_add, QtWidgets.QTableWidgetItem(str(column_to_add)))

    def clear_table(self):

        status = msg_box_ok_cancel("Clear table will clear all the setting set in the table.\n\n"
                                   "Press 'OK' to clear the table.\n"
                                   "Press 'Cancel' to cancel the action.")
        if status:
            self.pushButton_StoreSequency.setDisabled(True)
            self.pushButton_AddEditSeq.setDisabled(True)
            self.pushButton_DelStep.setDisabled(True)

            exist_step = self.tableWidget.columnCount()
            print(exist_step)
            for step in range(exist_step):
                self.tableWidget.removeColumn(1)

    def add_edit_step(self):
        self.step_selected = self.tableWidget.currentColumn()
        if self.step_selected > 0:

            # Check is the column was edited before with data?
            read_column_data = []
            for row in range(self.rowCount):
                row_data = self.tableWidget.item(row, self.step_selected)
                if row_data:
                    read_column_data.append(row_data.text())

            self.addedit_table = AddEdit_Seq(self,
                                             step_selected=self.step_selected,
                                             selected_equipment=self.selected_equipment,
                                             previous_setting=read_column_data)
            self.addedit_table.show()

        else:
            msg_box_ok("Please select any row from the required STEP column by clicking on one of the STEP's cell")

    def fillup_table(self, list_input):
        for row in range(self.rowCount):
            self.tableWidget.setItem(row, self.step_selected, QtWidgets.QTableWidgetItem(str(list_input[row])))
            if list_input[row] == "":
                self.tableWidget.item(row, self.step_selected).setBackground(QtGui.QColor('grey'))

    def delete_step(self):
        self.step_selected = self.tableWidget.currentColumn()
        if self.step_selected > 0:
            status = msg_box_ok_cancel(f"To delete Step: {self.step_selected}")
            if status:
                self.tableWidget.removeColumn(self.step_selected)
        else:
            msg_box_ok("Please select the 1x desire column to delete")

    def store_sequence(self):

        # -------------------Get info from table------------------------
        error_read_table, read_sequence, step_count = self.read_table()
        if error_read_table:
            msg_box_ok("Please fill up all the sequence setting before proceed!")
        else:
            # -------------------Get info from definition setting-------------------
            seq_name = self.lineEdit_prog_title.text()
            seq_no = self.spinBox_prog_no.text()
            seq_polarity = self.comboBox_polarity.currentText()
            seq_mode = self.comboBox_mode.currentText()
            seq_iteration = self.spinBox_iteration.text()
            seq_steps = str(step_count - 1)

            if self.lineEdit_prog_title.text() == "":
                seq_name = f'Sequence_{seq_no}'

            read_setting = [seq_name, seq_no, seq_polarity, seq_mode, seq_iteration, seq_steps]

            # Connect Equipment
            self.instrument.connect_equipment(self.selected_equipment)
            print(read_sequence)
            # Set sequence output
            status, error_msg = self.instrument.set_sequence_output(read_setting, read_sequence)

            if not status:
                msg_box_ok(f"{error_msg}\n\n"
                           "It may due to:\n"
                           "- Lost of connection with the equipment\n"
                           "- Incorrect sequence setting")

            # Set DC Parameter sequencing

    def read_table(self):
        self.columnCount = self.tableWidget.columnCount()                   # Inclusive of column used for description
        self.sequence_setting = []
        error = False

        for column in range(1, self.columnCount):
            row_item = [column]
            for row in range(self.rowCount):
                setting = self.tableWidget.item(row, column)
                if setting:
                    row_item.append(setting.text())
                else:
                    error = True
                    break
            if error:
                break
            else:
                self.sequence_setting.append(row_item)

        return error, self.sequence_setting, self.columnCount

    def run_sequence(self):
        # Get user input
        seq_no = self.spinBox_prog_no.text()

        # Connect the equipment
        self.instrument.connect_equipment(self.selected_equipment)

        # Enable read output and display
        self.read_thread = Thread(target=self.read_output)

        # Query for status of Equipment (is  running or not)
        run_status, data_query = self.instrument.run_sequence_query()

        if run_status:
            status_run_sequence = data_query.split(",", 4)[0]
            if status_run_sequence == "STOP":
                # Set Sequence Number to execute
                status, error_msg = self.instrument.run_sequence_output(seq_no)
                if not status:
                    msg_box_ok(f"{error_msg}\n\n"
                               "It may due to:\n"
                               "- Lost of connection with the equipment\n")
                else:
                    self.read_thread.start()
                    self.read_output_stat = True

            else:
                msg_box_ok("Error:\n\n"
                           "On-going Sequence is running.\n "
                           "Unable to start a new one!!")

        else:
            msg_box_ok(f"{data_query}\n\n"
                       "It may due to:\n"
                       "- Lost of connection with the equipment\n")

    def read_output(self):
        # Time delay for equipment to turn on first
        time.sleep(0.5)
        while self.read_output_stat:
            run_status, data_query = self.instrument.run_sequence_query()
            seq_run_status = data_query.split(",", 4)[0]

            if seq_run_status == "STOP":
                self.read_output_stat = False

            self.vout_read = self.instrument.read_output_supply()[0]
            self.iout_read = self.instrument.read_output_supply()[1]
            self.lcdNumber_Voltage.display(f'{self.vout_read}')
            self.lcdNumber_Current.display(f'{self.iout_read}')
        self.instrument.on_off_equipment(0)


# Add Edit Sequential Voltage UI
class AddEdit_Seq(QMainWindow, SEQ_AddEdit_UI.Ui_AddEdit_SEQ):
    def __init__(self, parent, step_selected, selected_equipment, previous_setting):
        super(AddEdit_Seq, self).__init__(parent)
        self.table = parent
        self.step_selected = step_selected
        self.selected_equipment = selected_equipment
        self.previous_setting = previous_setting
        self.setupUi(self)
        self.Step_Label.setText(str(step_selected))
        self.setting_preset()
        self.Cancel.clicked.connect(self.cancel)
        self.DCRamp_ONOFF.currentIndexChanged.connect(self.DCRamp_ON)
        self.ACSprImp_ONOFF.currentIndexChanged.connect(self.ACSpr_Imp_ON)
        self.ACSwpAmp_ONOFF.currentIndexChanged.connect(self.ACSwp_ON)
        self.ACFreqSwp_ONOFF.currentIndexChanged.connect(self.ACFreq_ON)
        self.Apply.clicked.connect(self.apply)

    def setting_preset(self):
        self.onlyfloat = QDoubleValidator()
        # self.onlyInt = QIntValidator()
        self.StepTime.setValidator(self.onlyfloat)
        self.StepDCV.setValidator(self.onlyfloat)
        self.DCRamp_StartLvl.setValidator(self.onlyfloat)
        self.DCRamp_StopLvl.setValidator(self.onlyfloat)
        self.ACSprImp_Vpp.setValidator(self.onlyfloat)
        self.ACSprImp_Freq.setValidator(self.onlyfloat)
        self.ACSprImp_Phase.setValidator(self.onlyfloat)
        self.ACSprImp_DutyCycle.setValidator(self.onlyfloat)
        self.ACSwpAmp_Start_Vpp.setValidator(self.onlyfloat)
        self.ACSwpAmp_Stop_Vpp.setValidator(self.onlyfloat)
        self.ACFreqSwp_StartFreq.setValidator(self.onlyfloat)
        self.ACFreqSwp_StopFreq.setValidator(self.onlyfloat)
        self.StepOut_ONOFF.addItems(["ON", "OFF"])
        self.DCRamp_ONOFF.addItems(["OFF", "ON"])
        self.TrigIn_ONOFF.addItems(["OFF", "ON"])
        self.TrigOut_ONOFF.addItems(["OFF", "ON"])
        self.ACSprImp_ONOFF.addItems(["OFF", "ON"])
        self.ACSprImp_Type.addItems(["SINe", "SQUare", "TRIangle"])
        self.ACSwpAmp_ONOFF.addItems(["OFF", "ON"])
        self.ACFreqSwp_ONOFF.addItems(["OFF", "ON"])
        self.ACFreqSwp_Mode.addItems(["LINear", "LOG"])
        self.DCRamp_StartLvl.setDisabled(True)
        self.DCRamp_StopLvl.setDisabled(True)
        self.ACSprImp_Type.setDisabled(True)
        self.ACSprImp_Vpp.setDisabled(True)
        self.ACSprImp_Freq.setDisabled(True)
        self.ACSprImp_Phase.setDisabled(True)
        self.ACSprImp_DutyCycle.setDisabled(True)
        self.ACSwpAmp_Start_Vpp.setDisabled(True)
        self.ACSwpAmp_Stop_Vpp.setDisabled(True)
        self.ACFreqSwp_Mode.setDisabled(True)
        self.ACFreqSwp_StartFreq.setDisabled(True)
        self.ACFreqSwp_StopFreq.setDisabled(True)

        if self.previous_setting:
            self.StepTime.setText(self.previous_setting[0])
            self.StepDCV.setText(self.previous_setting[1])
            if self.previous_setting[5] == "OFF":
                self.StepOut_ONOFF.setCurrentIndex(1)
            if self.previous_setting[2] == "ON":
                self.DCRamp_ONOFF.setCurrentIndex(1)
                self.DCRamp_StartLvl.setText(self.previous_setting[3])
                self.DCRamp_StartLvl.setDisabled(False)
                self.DCRamp_StopLvl.setText(self.previous_setting[4])
                self.DCRamp_StopLvl.setDisabled(False)
            if self.previous_setting[6] == "ON":
                self.TrigOut_ONOFF.setCurrentIndex(1)
            if self.previous_setting[7] == "ON":
                self.TrigIn_ONOFF.setCurrentIndex(1)
            if self.previous_setting[8] == "ON":
                self.ACSprImp_ONOFF.setCurrentIndex(1)
                self.ACSprImp_Type.setDisabled(False)
                self.ACSprImp_Vpp.setDisabled(False)
                self.ACSprImp_Freq.setDisabled(False)
                self.ACSprImp_Phase.setDisabled(False)
                self.ACSprImp_DutyCycle.setDisabled(False)
                if self.previous_setting[9] == "SINe":
                    self.ACSprImp_Type.setCurrentIndex(0)
                elif self.previous_setting[9] == "SQUare":
                    self.ACSprImp_Type.setCurrentIndex(1)
                else:
                    self.ACSprImp_Type.setCurrentIndex(2)
                self.ACSprImp_Vpp.setText(self.previous_setting[10])
                self.ACSprImp_Freq.setText(self.previous_setting[11])
                self.ACSprImp_Phase.setText(self.previous_setting[12])
                self.ACSprImp_DutyCycle.setText(self.previous_setting[13])
            if self.previous_setting[14] == "ON":
                self.ACSwpAmp_ONOFF.setCurrentIndex(1)
                self.ACSwpAmp_Start_Vpp.setDisabled(False)
                self.ACSwpAmp_Stop_Vpp.setDisabled(False)
                self.ACSwpAmp_Start_Vpp.setText(self.previous_setting[15])
                self.ACSwpAmp_Stop_Vpp.setText(self.previous_setting[16])
            if self.previous_setting[17] == "ON":
                self.ACFreqSwp_ONOFF.setCurrentIndex(1)
                self.ACFreqSwp_Mode.setDisabled(False)
                self.ACFreqSwp_StartFreq.setDisabled(False)
                self.ACFreqSwp_StopFreq.setDisabled(False)
                if self.previous_setting[18] == "LINear":
                    self.ACFreqSwp_Mode.setCurrentIndex(0)
                else:
                    self.ACFreqSwp_Mode.setCurrentIndex(1)
                self.ACFreqSwp_StartFreq.setText(self.previous_setting[19])
                self.ACFreqSwp_StopFreq.setText(self.previous_setting[20])

    def DCRamp_ON(self):
        if self.DCRamp_ONOFF.currentIndex() == 1:
            self.DCRamp_StartLvl.setDisabled(False)
            self.DCRamp_StopLvl.setDisabled(False)
        else:
            self.DCRamp_StartLvl.setDisabled(True)
            self.DCRamp_StopLvl.setDisabled(True)

    def ACSpr_Imp_ON(self):
        if self.ACSprImp_ONOFF.currentIndex() == 1:
            self.ACSprImp_Type.setDisabled(False)
            self.ACSprImp_Vpp.setDisabled(False)
            self.ACSprImp_Freq.setDisabled(False)
            self.ACSprImp_Phase.setDisabled(False)
            self.ACSprImp_DutyCycle.setDisabled(False)
        else:
            self.ACSprImp_Type.setDisabled(True)
            self.ACSprImp_Vpp.setDisabled(True)
            self.ACSprImp_Freq.setDisabled(True)
            self.ACSprImp_Phase.setDisabled(True)
            self.ACSprImp_DutyCycle.setDisabled(True)

    def ACSwp_ON(self):
        if self.ACSwpAmp_ONOFF.currentIndex() == 1:
            self.ACSwpAmp_Start_Vpp.setDisabled(False)
            self.ACSwpAmp_Stop_Vpp.setDisabled(False)
        else:
            self.ACSwpAmp_Start_Vpp.setDisabled(True)
            self.ACSwpAmp_Stop_Vpp.setDisabled(True)

    def ACFreq_ON(self):
        if self.ACFreqSwp_ONOFF.currentIndex() == 1:
            self.ACFreqSwp_Mode.setDisabled(False)
            self.ACFreqSwp_StartFreq.setDisabled(False)
            self.ACFreqSwp_StopFreq.setDisabled(False)
        else:
            self.ACFreqSwp_Mode.setDisabled(True)
            self.ACFreqSwp_StartFreq.setDisabled(True)
            self.ACFreqSwp_StopFreq.setDisabled(True)

    def cancel(self):
        status = msg_box_ok_cancel("Cancel changes?")
        if status:
            self.close()

    # ----------------------------------- Validate User Input --------------------------------------------------------
    def apply(self):
        error = 0
        self.user_seq_input = []

        # -------------------------------- DC Output Validity ------------------------------------------------------
        if self.StepTime.text() == "":
            error += 1
            self.StepTime.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
        else:
            self.StepTime.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
            self.user_seq_input.append(self.StepTime.text())

        if self.StepDCV.text() == "":
            error += 1
            self.StepDCV.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
        else:
            if float(self.StepDCV.text()) < 22:
                self.user_seq_input.append(self.StepDCV.text())
                self.StepDCV.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
            else:
                error += 1
                self.StepDCV.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 0);}")

        # --------------------------------- DC RAMP data Validity --------------------------------------------------
        self.user_seq_input.append(self.DCRamp_ONOFF.currentText())
        if self.DCRamp_ONOFF.currentIndex() == 1:
            if self.DCRamp_StartLvl.text() == "":
                error += 1
                self.DCRamp_StartLvl.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
            else:
                if float(self.DCRamp_StartLvl.text()) < 22:
                    self.DCRamp_StartLvl.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
                    self.user_seq_input.append(self.DCRamp_StartLvl.text())
                else:
                    error += 1
                    self.DCRamp_StartLvl.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 0);}")

            if self.DCRamp_StopLvl.text() == "":
                error += 1
                self.DCRamp_StopLvl.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
            else:
                if float(self.DCRamp_StopLvl.text()) < 22:
                    self.DCRamp_StopLvl.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
                    self.user_seq_input.append(self.DCRamp_StopLvl.text())
                else:
                    error += 1
                    self.DCRamp_StopLvl.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 0);}")
        else:
            for x in range(2):
                self.user_seq_input.append("")

        self.user_seq_input.append(self.StepOut_ONOFF.currentText())

        # --------------------------------- Trigger data Input -------------------------------------------------
        self.user_seq_input.append(self.TrigOut_ONOFF.currentText())
        self.user_seq_input.append(self.TrigIn_ONOFF.currentText())

        # --------------------------------- AC SuperImpose on DC Input --------------------------------------------
        self.user_seq_input.append(self.ACSprImp_ONOFF.currentText())
        if self.ACSprImp_ONOFF.currentIndex() == 1:
            self.user_seq_input.append(self.ACSprImp_Type.currentText())
            if self.ACSprImp_Vpp.text() == "":
                error += 1
                self.ACSprImp_Vpp.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
            else:
                if float(self.ACSprImp_Vpp.text()) < 22:
                    self.ACSprImp_Vpp.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
                    self.user_seq_input.append(self.ACSprImp_Vpp.text())
                else:
                    error += 1
                    self.ACSprImp_Vpp.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 0);}")

            if self.ACSprImp_Freq.text() == "":
                error += 1
                self.ACSprImp_Freq.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
            else:
                self.ACSprImp_Freq.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
                self.user_seq_input.append(self.ACSprImp_Freq.text())

            if self.ACSprImp_Phase.text() == "":
                error += 1
                self.ACSprImp_Phase.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
            else:
                self.ACSprImp_Phase.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
                self.user_seq_input.append(self.ACSprImp_Phase.text())

            if self.ACSprImp_DutyCycle.text() == "":
                error += 1
                self.ACSprImp_DutyCycle.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
            else:
                self.ACSprImp_DutyCycle.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
                self.user_seq_input.append(self.ACSprImp_DutyCycle.text())
        else:
            for x in range(5):
                self.user_seq_input.append("")

        # -------------------------------------- AC Sweep on DC Input -------------------------------------------
        self.user_seq_input.append(self.ACSwpAmp_ONOFF.currentText())
        if self.ACSwpAmp_ONOFF.currentIndex() == 1:
            if self.ACSwpAmp_Start_Vpp.text() == "":
                error += 1
                self.ACSwpAmp_Start_Vpp.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
            else:
                if float(self.ACSwpAmp_Start_Vpp.text()) < 22:
                    self.ACSwpAmp_Start_Vpp.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
                    self.user_seq_input.append(self.ACSwpAmp_Start_Vpp.text())
                else:
                    error += 1
                    self.ACSwpAmp_Start_Vpp.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 0);}")

            if self.ACSwpAmp_Stop_Vpp.text() == "":
                error += 1
                self.ACSwpAmp_Stop_Vpp.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
            else:
                if float(self.ACSwpAmp_Stop_Vpp.text()) < 22:
                    self.ACSwpAmp_Stop_Vpp.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
                    self.user_seq_input.append(self.ACSwpAmp_Stop_Vpp.text())
                else:
                    error += 1
                    self.ACSwpAmp_Stop_Vpp.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 0);}")

        else:
            for x in range(2):
                self.user_seq_input.append("")

        # -------------------------------------- AC Frequency Sweep on DC Input ---------------------------------
        self.user_seq_input.append(self.ACFreqSwp_ONOFF.currentText())
        if self.ACFreqSwp_ONOFF.currentIndex() == 1:

            self.user_seq_input.append(self.ACFreqSwp_Mode.currentText())

            if self.ACFreqSwp_StartFreq.text() == "":
                error += 1
                self.ACFreqSwp_StartFreq.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
            else:
                self.ACFreqSwp_StartFreq.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
                self.user_seq_input.append(self.ACFreqSwp_StartFreq.text())

            if self.ACFreqSwp_StopFreq.text() == "":
                error += 1
                self.ACFreqSwp_StopFreq.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
            else:
                self.ACFreqSwp_StopFreq.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
                self.user_seq_input.append(self.ACFreqSwp_StopFreq.text())
        else:
            for x in range(3):
                self.user_seq_input.append("")

        if error is not 0:
            msg_box_ok("Please fill-up the empty RED boxes\"\n"
                       "Please update/ change the incorrect value in YELLOW boxes")
        else:
            self.close()
            self.table.fillup_table(self.user_seq_input)



