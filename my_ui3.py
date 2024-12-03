from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(551, 745)
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(80, 140, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.Sold_label = QtWidgets.QLabel(Form)
        self.Sold_label.setGeometry(QtCore.QRect(70, 170, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Sold_label.setFont(font)
        self.Sold_label.setObjectName("Sold_label")
        self.profit_label = QtWidgets.QLabel(Form)
        self.profit_label.setGeometry(QtCore.QRect(120, 190, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.profit_label.setFont(font)
        self.profit_label.setObjectName("profit_label")
        self.List_pople = QtWidgets.QListView(Form)
        self.List_pople.setGeometry(QtCore.QRect(140, 350, 256, 371))
        self.List_pople.setObjectName("List_pople")
        self.List_pepople_label = QtWidgets.QLabel(Form)
        self.List_pepople_label.setGeometry(QtCore.QRect(210, 320, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.List_pepople_label.setFont(font)
        self.List_pepople_label.setObjectName("List_pepople_label")
        self.movie_label = QtWidgets.QLabel(Form)
        self.movie_label.setGeometry(QtCore.QRect(180, 140, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.movie_label.setFont(font)
        self.movie_label.setObjectName("movie_label")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(180, 170, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(180, 200, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(280, 140, 73, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "Movie title"))
        self.Sold_label.setText(_translate("Form", "Sold tickets"))
        self.profit_label.setText(_translate("Form", "Profit"))
        self.List_pepople_label.setText(_translate("Form", "List of people"))
        self.movie_label.setText(_translate("Form", "None"))
        self.label_6.setText(_translate("Form", "None"))
        self.label_7.setText(_translate("Form", "None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
