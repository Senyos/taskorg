# Form implementation generated from reading ui file './app/ui/ui/write_note_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WriteWindow(object):
    def setupUi(self, WriteWindow):
        WriteWindow.setObjectName("WriteWindow")
        WriteWindow.resize(641, 183)
        self.main_widget_note = QtWidgets.QWidget(parent=WriteWindow)
        self.main_widget_note.setObjectName("main_widget_note")
        self.gridLayout = QtWidgets.QGridLayout(self.main_widget_note)
        self.gridLayout.setObjectName("gridLayout")
        self.body = QtWidgets.QVBoxLayout()
        self.body.setObjectName("body")
        self.theme = QtWidgets.QHBoxLayout()
        self.theme.setObjectName("theme")
        self.l_theme = QtWidgets.QLabel(parent=self.main_widget_note)
        self.l_theme.setObjectName("l_theme")
        self.theme.addWidget(self.l_theme)
        self.t_theme = QtWidgets.QLineEdit(parent=self.main_widget_note)
        self.t_theme.setObjectName("t_theme")
        self.theme.addWidget(self.t_theme)
        self.body.addLayout(self.theme)
        self.note = QtWidgets.QHBoxLayout()
        self.note.setObjectName("note")
        self.l_note = QtWidgets.QLabel(parent=self.main_widget_note)
        self.l_note.setObjectName("l_note")
        self.note.addWidget(self.l_note)
        self.t_note = QtWidgets.QLineEdit(parent=self.main_widget_note)
        self.t_note.setObjectName("t_note")
        self.note.addWidget(self.t_note)
        self.body.addLayout(self.note)
        self.date = QtWidgets.QHBoxLayout()
        self.date.setObjectName("date")
        self.l_date = QtWidgets.QLabel(parent=self.main_widget_note)
        self.l_date.setObjectName("l_date")
        self.date.addWidget(self.l_date)
        self.t_date = QtWidgets.QDateEdit(parent=self.main_widget_note)
        self.t_date.setCalendarPopup(True)
        self.t_date.setObjectName("t_date")
        self.date.addWidget(self.t_date)
        self.body.addLayout(self.date)
        self.line = QtWidgets.QFrame(parent=self.main_widget_note)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.body.addWidget(self.line)
        self.b_createnote = QtWidgets.QPushButton(parent=self.main_widget_note)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_createnote.sizePolicy().hasHeightForWidth())
        self.b_createnote.setSizePolicy(sizePolicy)
        self.b_createnote.setObjectName("b_createnote")
        self.body.addWidget(self.b_createnote)
        self.gridLayout.addLayout(self.body, 0, 0, 1, 1)
        WriteWindow.setCentralWidget(self.main_widget_note)

        self.retranslateUi(WriteWindow)
        QtCore.QMetaObject.connectSlotsByName(WriteWindow)

    def retranslateUi(self, WriteWindow):
        _translate = QtCore.QCoreApplication.translate
        WriteWindow.setWindowTitle(_translate("WriteWindow", "Написать заметку"))
        self.l_theme.setText(_translate("WriteWindow", "Тема"))
        self.l_note.setText(_translate("WriteWindow", "Заметка"))
        self.l_date.setText(_translate("WriteWindow", "Когда выполнить"))
        self.b_createnote.setText(_translate("WriteWindow", "Создать заметку"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WriteWindow = QtWidgets.QMainWindow()
    ui = Ui_WriteWindow()
    ui.setupUi(WriteWindow)
    WriteWindow.show()
    sys.exit(app.exec())
