# Form implementation generated from reading ui file './app/ui/ui/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 526)
        self.main_widget = QtWidgets.QWidget(parent=MainWindow)
        self.main_widget.setObjectName("main_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.main_widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textwidget = QtWidgets.QVBoxLayout()
        self.textwidget.setObjectName("textwidget")
        self.titletext = QtWidgets.QHBoxLayout()
        self.titletext.setObjectName("titletext")
        self.t_title = QtWidgets.QLineEdit(parent=self.main_widget)
        self.t_title.setReadOnly(True)
        self.t_title.setObjectName("t_title")
        self.titletext.addWidget(self.t_title)
        self.textwidget.addLayout(self.titletext)
        self.contenttext = QtWidgets.QHBoxLayout()
        self.contenttext.setObjectName("contenttext")
        self.t_content = QtWidgets.QTextEdit(parent=self.main_widget)
        self.t_content.setReadOnly(True)
        self.t_content.setObjectName("t_content")
        self.contenttext.addWidget(self.t_content)
        self.textwidget.addLayout(self.contenttext)
        self.horizontalLayout_3.addLayout(self.textwidget)
        self.lastnotes_buttons = QtWidgets.QVBoxLayout()
        self.lastnotes_buttons.setObjectName("lastnotes_buttons")
        self.l_ttlabel = QtWidgets.QLabel(parent=self.main_widget)
        self.l_ttlabel.setObjectName("l_ttlabel")
        self.lastnotes_buttons.addWidget(self.l_ttlabel)
        self.b_todaynote = QtWidgets.QPushButton(parent=self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_todaynote.sizePolicy().hasHeightForWidth())
        self.b_todaynote.setSizePolicy(sizePolicy)
        self.b_todaynote.setObjectName("b_todaynote")
        self.lastnotes_buttons.addWidget(self.b_todaynote)
        self.b_tommorownote = QtWidgets.QPushButton(parent=self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_tommorownote.sizePolicy().hasHeightForWidth())
        self.b_tommorownote.setSizePolicy(sizePolicy)
        self.b_tommorownote.setObjectName("b_tommorownote")
        self.lastnotes_buttons.addWidget(self.b_tommorownote)
        self.line = QtWidgets.QFrame(parent=self.main_widget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.lastnotes_buttons.addWidget(self.line)
        self.t_datenote = QtWidgets.QDateEdit(parent=self.main_widget)
        self.t_datenote.setCalendarPopup(True)
        self.t_datenote.setObjectName("t_datenote")
        self.lastnotes_buttons.addWidget(self.t_datenote)
        self.b_datenote = QtWidgets.QPushButton(parent=self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_datenote.sizePolicy().hasHeightForWidth())
        self.b_datenote.setSizePolicy(sizePolicy)
        self.b_datenote.setObjectName("b_datenote")
        self.lastnotes_buttons.addWidget(self.b_datenote)
        self.horizontalLayout_3.addLayout(self.lastnotes_buttons)
        self.main_buttons = QtWidgets.QVBoxLayout()
        self.main_buttons.setObjectName("main_buttons")
        self.b_writenote = QtWidgets.QPushButton(parent=self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_writenote.sizePolicy().hasHeightForWidth())
        self.b_writenote.setSizePolicy(sizePolicy)
        self.b_writenote.setObjectName("b_writenote")
        self.main_buttons.addWidget(self.b_writenote)
        self.b_findnote = QtWidgets.QPushButton(parent=self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_findnote.sizePolicy().hasHeightForWidth())
        self.b_findnote.setSizePolicy(sizePolicy)
        self.b_findnote.setObjectName("b_findnote")
        self.main_buttons.addWidget(self.b_findnote)
        self.b_deletenote = QtWidgets.QPushButton(parent=self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_deletenote.sizePolicy().hasHeightForWidth())
        self.b_deletenote.setSizePolicy(sizePolicy)
        self.b_deletenote.setAutoFillBackground(False)
        self.b_deletenote.setObjectName("b_deletenote")
        self.main_buttons.addWidget(self.b_deletenote)
        self.horizontalLayout_3.addLayout(self.main_buttons)
        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "taskorg"))
        self.l_ttlabel.setText(_translate("MainWindow", "Заметки на:"))
        self.b_todaynote.setText(_translate("MainWindow", "Сегодня"))
        self.b_tommorownote.setText(_translate("MainWindow", "Завтра"))
        self.b_datenote.setText(_translate("MainWindow", "На дату"))
        self.b_writenote.setText(_translate("MainWindow", "Написать заметку"))
        self.b_findnote.setText(_translate("MainWindow", "Найти заметки"))
        self.b_deletenote.setText(_translate("MainWindow", "Удалить заметки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
