# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\02_SEQ_Console.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 807)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 260))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setMinimumSize(QtCore.QSize(400, 0))
        self.frame.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_prog_title = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_prog_title.setFont(font)
        self.lineEdit_prog_title.setObjectName("lineEdit_prog_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_prog_title)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_polarity = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_polarity.setFont(font)
        self.comboBox_polarity.setObjectName("comboBox_polarity")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_polarity)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBox_mode = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_mode.setFont(font)
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_mode)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinBox_iteration = QtWidgets.QSpinBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_iteration.setFont(font)
        self.spinBox_iteration.setObjectName("spinBox_iteration")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_iteration)
        self.spinBox_prog_no = QtWidgets.QSpinBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_prog_no.setFont(font)
        self.spinBox_prog_no.setMinimum(1)
        self.spinBox_prog_no.setMaximum(16)
        self.spinBox_prog_no.setObjectName("spinBox_prog_no")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_prog_no)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.pushButton_CreateTable = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_CreateTable.setFont(font)
        self.pushButton_CreateTable.setStyleSheet("background: #f0f0f0")
        self.pushButton_CreateTable.setObjectName("pushButton_CreateTable")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.pushButton_CreateTable)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.pushButton_AddStep = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_AddStep.setFont(font)
        self.pushButton_AddStep.setStyleSheet("background: #f0f0f0")
        self.pushButton_AddStep.setObjectName("pushButton_AddStep")
        self.horizontalLayout_3.addWidget(self.pushButton_AddStep)
        self.pushButton_EditStep = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_EditStep.setFont(font)
        self.pushButton_EditStep.setStyleSheet("background: #f0f0f0")
        self.pushButton_EditStep.setObjectName("pushButton_EditStep")
        self.horizontalLayout_3.addWidget(self.pushButton_EditStep)
        self.pushButton_ClearTable = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_ClearTable.setFont(font)
        self.pushButton_ClearTable.setStyleSheet("background: #f0f0f0")
        self.pushButton_ClearTable.setObjectName("pushButton_ClearTable")
        self.horizontalLayout_3.addWidget(self.pushButton_ClearTable)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.pushButton_Back = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Back.setFont(font)
        self.pushButton_Back.setStyleSheet("background: #f0f0f0")
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.horizontalLayout_3.addWidget(self.pushButton_Back)
        self.pushButton_RunSequence = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_RunSequence.setFont(font)
        self.pushButton_RunSequence.setStyleSheet("background: #f0f0f0")
        self.pushButton_RunSequence.setObjectName("pushButton_RunSequence")
        self.horizontalLayout_3.addWidget(self.pushButton_RunSequence)
        self.pushButton_StoreSequency = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_StoreSequency.setFont(font)
        self.pushButton_StoreSequency.setStyleSheet("background: #f0f0f0")
        self.pushButton_StoreSequency.setObjectName("pushButton_StoreSequency")
        self.horizontalLayout_3.addWidget(self.pushButton_StoreSequency)
        spacerItem8 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(22)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(17, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(18, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(19, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(20, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(21, 0, item)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout.addWidget(self.frame_3)
        spacerItem11 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 21))
        self.menubar.setObjectName("menubar")
        self.menuNavigate = QtWidgets.QMenu(self.menubar)
        self.menuNavigate.setObjectName("menuNavigate")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBack = QtWidgets.QAction(MainWindow)
        self.actionBack.setObjectName("actionBack")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuNavigate.addAction(self.actionBack)
        self.menuNavigate.addAction(self.actionExit)
        self.menubar.addAction(self.menuNavigate.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KiKusui PZA20-20 PS Console: SEQ Mode"))
        self.label.setText(_translate("MainWindow", "Programmable (Arbitrary) Supply "))
        self.label_2.setText(_translate("MainWindow", "Title"))
        self.label_3.setText(_translate("MainWindow", "Prog No."))
        self.label_4.setText(_translate("MainWindow", "Polarity"))
        self.label_5.setText(_translate("MainWindow", "Mode"))
        self.label_6.setText(_translate("MainWindow", "Iterations"))
        self.label_7.setText(_translate("MainWindow", "Steps"))
        self.pushButton_CreateTable.setText(_translate("MainWindow", "Create Table"))
        self.label_8.setText(_translate("MainWindow", "Please \"Create Table\" with needed \"Steps\" before proceed with adding info to the table."))
        self.pushButton_AddStep.setText(_translate("MainWindow", "Add Sequence"))
        self.pushButton_EditStep.setText(_translate("MainWindow", "Edit Sequence"))
        self.pushButton_ClearTable.setText(_translate("MainWindow", "Clear Table"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.pushButton_RunSequence.setText(_translate("MainWindow", "Run Sequence"))
        self.pushButton_StoreSequency.setText(_translate("MainWindow", "Store Sequence"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "STEP"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "TIME"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "DC"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "DC_RAMP"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "DC_RAMP_START"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "DC_RAMP_STOP"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "OUTPUT_STATE"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "TRIG_OUT"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "TRIG_IN"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "AC"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "FUNC"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "AMPL"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "FREQ"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "PHASE"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "DUTY"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "AMPL_SWEEP"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "AMPL_START"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "AMPL_STOP"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "FREQ_SWEEP"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "FREQ_MODE"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "FREQ_START"))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "FREQ_STOP"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Description"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Step Number"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Step Execution Time (s)"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "DC Voltage Level (V)"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "DC Ramp (ON/OFF)"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "DC Start level (V)"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "DC Stop level (V)"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", "Output State (ON/OFF)"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", "Trigger Signal Out (ON/OFF)"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("MainWindow", "Trigger Signal In (ON/OFF)"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainWindow", "AC Superimpose DC (ON/OFF)"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("MainWindow", "AC Signal waveform (Type)"))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("MainWindow", "AC Signal amplitude (Vp-p)"))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("MainWindow", "AC Signal Frequency (Hz)"))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("MainWindow", "AC Start Phase Angle (deg)"))
        item = self.tableWidget.item(14, 0)
        item.setText(_translate("MainWindow", "SquareWave Duty Ratio (%)"))
        item = self.tableWidget.item(15, 0)
        item.setText(_translate("MainWindow", "AC Sweep Amp. (ON/OFF))"))
        item = self.tableWidget.item(16, 0)
        item.setText(_translate("MainWindow", "AC Sweep Start Amp. (Vp-p)"))
        item = self.tableWidget.item(17, 0)
        item.setText(_translate("MainWindow", "AC Sweep Stop Amp. (Vp-p)"))
        item = self.tableWidget.item(18, 0)
        item.setText(_translate("MainWindow", "AC Freq Sweep (ON/OFF)"))
        item = self.tableWidget.item(19, 0)
        item.setText(_translate("MainWindow", "AC Freq Sweep Mode (Mode)"))
        item = self.tableWidget.item(20, 0)
        item.setText(_translate("MainWindow", "AC Freq Sweep Start (Hz)"))
        item = self.tableWidget.item(21, 0)
        item.setText(_translate("MainWindow", "AC Freq Sweep Stop (Hz)"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menuNavigate.setTitle(_translate("MainWindow", "Navigate"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionBack.setText(_translate("MainWindow", "Back"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())