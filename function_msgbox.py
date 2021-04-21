from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QDateTime
from PyQt5 import QtCore, uic
from UIpy import MsgBoxOk, MsgBoxOkCancel, NewEntry_dialog, NewDropList_dialog, MsgBoxAutoClose, NewCalender_dialog, about


class MsgBoxAutoClose_UI(QDialog, MsgBoxAutoClose.Ui_msgboxautoclose):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def msgbox_auto_close(self, input_text):
        self.timer = QtCore.QTimer(self)
        self.label.setText(input_text)
        self.timer.setInterval(1500)
        self.timer.timeout.connect(self.changeContent)
        self.timer.start()

    def changeContent(self):
        self.close()


class MsgBoxOK_UI(QDialog, MsgBoxOk.Ui_msgboxok):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def msgbox_ok_set_text(self, input_text):
        self.label.setText(input_text)


class MsgBoxOKCancel_UI(QDialog, MsgBoxOkCancel.Ui_msgboxokcancel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def msgbox_ok_cancel_set_text(self, input_text):
        self.msgboxokcancel_label.setText(input_text)


class NewEntry_UI(QDialog, NewEntry_dialog.Ui_new_entry_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class NewDropList_UI(QDialog, NewDropList_dialog.Ui_new_droplist_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class NewCalender_UI(QDialog, NewCalender_dialog.Ui_new_droplist_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class about_UI(QDialog, about.Ui_Dialog_help):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_email.setText("<a href='mailto:chenhui_k029@hotmail.com?"
                                 "subject=Support for Kikusui PBZ-2020 control interface&"
                                 "body=Hi support, \nI would like to seek for help on ..\n'"
                                 ">Click here to sent an email for support regarding the control interface.")
        self.label_email.setOpenExternalLinks(True)


def msg_box_ok(input_text=None):
    print_try = MsgBoxOK_UI()
    print_try.msgbox_ok_set_text(input_text)
    print_try.exec_()


def msg_box_ok_cancel(input_text=None):
    print_try_2 = MsgBoxOKCancel_UI()
    print_try_2.msgbox_ok_cancel_set_text(input_text)
    return_result = print_try_2.exec_()
    return return_result


def msg_box_auto_close(input_text=None):
    print_try_3 = MsgBoxAutoClose_UI()
    print_try_3.msgbox_auto_close(input_text)
    return_result = print_try_3.exec_()
    return return_result


def new_entry_get_text():
    new_entry_display = NewEntry_UI()
    clicked_ok_cancel = new_entry_display.exec_()
    if clicked_ok_cancel:
        return clicked_ok_cancel, new_entry_display.lineEdit_new_entry.displayText()
    else:
        return clicked_ok_cancel, ""


def new_drop_list(input_items=None):
    if input_items is None:
        input_items = []
    new_droplist_box = NewDropList_UI()
    new_droplist_box.comboBox.clear()
    for input_item in input_items:
        new_droplist_box.comboBox.addItem(input_item)
    clicked_ok_cancel = new_droplist_box.exec_()
    if clicked_ok_cancel:
        return clicked_ok_cancel, new_droplist_box.comboBox.currentText()
    else:
        return clicked_ok_cancel, ""


def new_calender_get_date():
    new_get_date = NewCalender_UI()
    clicked_ok_cancel = new_get_date.exec_()
    if clicked_ok_cancel:
        return clicked_ok_cancel, new_get_date.calendarWidget.selectedDate().toPyDate()
    else:
        return clicked_ok_cancel, ""


def about_show():
    about_help = about_UI()
    about_help.exec_()