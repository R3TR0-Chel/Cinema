from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Movie_report(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 800)
        Form.setStyleSheet(
            """
            #Form {
                background-image: url('./images/ackground.jpg');
                background-position: center;
                background-repeat: no-repeat;
            }
            """
        )
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(240, 50, 300, 90))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(250, 470, 256, 281))
        self.listView.setObjectName("listView")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(160, 190, 421, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_output = QtWidgets.QLabel(self.frame)
        self.title_output.setGeometry(QtCore.QRect(150, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_output.setFont(font)
        self.title_output.setObjectName("title_output")
        self.Movie_title = QtWidgets.QLabel(self.frame)
        self.Movie_title.setGeometry(QtCore.QRect(40, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Movie_title.setFont(font)
        self.Movie_title.setObjectName("Movie_title")
        self.title_output_2 = QtWidgets.QLabel(self.frame)
        self.title_output_2.setGeometry(QtCore.QRect(150, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_output_2.setFont(font)
        self.title_output_2.setObjectName("title_output_2")
        self.quantity_title = QtWidgets.QLabel(self.frame)
        self.quantity_title.setGeometry(QtCore.QRect(40, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.quantity_title.setFont(font)
        self.quantity_title.setObjectName("quantity_title")
        self.title_output_3 = QtWidgets.QLabel(self.frame)
        self.title_output_3.setGeometry(QtCore.QRect(150, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_output_3.setFont(font)
        self.title_output_3.setObjectName("title_output_3")
        self.seat_label = QtWidgets.QLabel(self.frame)
        self.seat_label.setGeometry(QtCore.QRect(40, 170, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.seat_label.setFont(font)
        self.seat_label.setObjectName("seat_label")
        self.People_label = QtWidgets.QLabel(self.frame)
        self.People_label.setGeometry(QtCore.QRect(40, 230, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.People_label.setFont(font)
        self.People_label.setObjectName("People_label")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(230, 70, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.frame.raise_()
        self.title.raise_()
        self.listView.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "Moviepoint"))
        self.title_output.setText(_translate("Form", "None"))
        self.Movie_title.setText(_translate("Form", "Title"))
        self.title_output_2.setText(_translate("Form", "None"))
        self.quantity_title.setText(_translate("Form", "Quantity:"))
        self.title_output_3.setText(_translate("Form", "None"))
        self.seat_label.setText(_translate("Form", "Seats"))
        self.People_label.setText(_translate("Form", "People"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Movie_report = QtWidgets.QWidget()
    ui = Ui_Movie_report()
    ui.setupUi(Movie_report)
    Movie_report.show()
    sys.exit(app.exec_())