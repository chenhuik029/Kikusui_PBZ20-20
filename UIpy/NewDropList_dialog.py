# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '13_list_select_ok_cancel.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_new_droplist_dialog(object):
    def setupUi(self, new_droplist_dialog):
        new_droplist_dialog.setObjectName("new_droplist_dialog")
        new_droplist_dialog.resize(350, 130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(new_droplist_dialog.sizePolicy().hasHeightForWidth())
        new_droplist_dialog.setSizePolicy(sizePolicy)
        new_droplist_dialog.setMinimumSize(QtCore.QSize(350, 130))
        new_droplist_dialog.setMaximumSize(QtCore.QSize(350, 130))
        self.verticalLayout = QtWidgets.QVBoxLayout(new_droplist_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.msgboxokcancel_label = QtWidgets.QLabel(new_droplist_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgboxokcancel_label.sizePolicy().hasHeightForWidth())
        self.msgboxokcancel_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.msgboxokcancel_label.setFont(font)
        self.msgboxokcancel_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msgboxokcancel_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.msgboxokcancel_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.msgboxokcancel_label.setObjectName("msgboxokcancel_label")
        self.verticalLayout_2.addWidget(self.msgboxokcancel_label)
        self.comboBox = QtWidgets.QComboBox(new_droplist_dialog)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(new_droplist_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.dialogButtonBox.setFont(font)
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.verticalLayout.addWidget(self.dialogButtonBox)

        self.retranslateUi(new_droplist_dialog)
        self.dialogButtonBox.accepted.connect(new_droplist_dialog.accept)
        self.dialogButtonBox.rejected.connect(new_droplist_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(new_droplist_dialog)

    def retranslateUi(self, new_droplist_dialog):
        _translate = QtCore.QCoreApplication.translate
        new_droplist_dialog.setWindowTitle(_translate("new_droplist_dialog", "Info"))
        self.msgboxokcancel_label.setText(_translate("new_droplist_dialog", "New Entry:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_droplist_dialog = QtWidgets.QDialog()
    ui = Ui_new_droplist_dialog()
    ui.setupUi(new_droplist_dialog)
    new_droplist_dialog.show()
    sys.exit(app.exec_())
