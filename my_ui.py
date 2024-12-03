
from PyQt5 import QtCore, QtGui, QtWidgets
from my_ui2 import Ui_Form2 
from Client_class import Client


class Ui_Form(object):
    def __init__(self):
        self.users = {}
        self.ticket_window = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(614, 572)
        self.Log_in_button = QtWidgets.QPushButton(Form)
        self.Log_in_button.setGeometry(QtCore.QRect(220, 350, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Log_in_button.setFont(font)
        self.Log_in_button.setObjectName("Log_in_button")
        self.Log_in_button.clicked.connect(self.on_Log_in_button_clicked)  # Убраны скобки

        self.Captcha_button = QtWidgets.QPushButton(Form)
        self.Captcha_button.setGeometry(QtCore.QRect(220, 410, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Captcha_button.setFont(font)
        self.Captcha_button.setObjectName("Captcha_button")

        self.New_user_button = QtWidgets.QPushButton(Form)
        self.New_user_button.setGeometry(QtCore.QRect(220, 470, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.New_user_button.setFont(font)
        self.New_user_button.setObjectName("New_user_button")
        self.New_user_button.clicked.connect(self.on_new_user_button_clicked)

        self.Password_label = QtWidgets.QLabel(Form)
        self.Password_label.setGeometry(QtCore.QRect(110, 260, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Password_label.setFont(font)
        self.Password_label.setObjectName("Password_label")

        self.User_name_label = QtWidgets.QLabel(Form)
        self.User_name_label.setGeometry(QtCore.QRect(100, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.User_name_label.setFont(font)
        self.User_name_label.setObjectName("User_name_label")

        self.user_input = QtWidgets.QLineEdit(Form)
        self.user_input.setGeometry(QtCore.QRect(200, 210, 221, 31))
        self.user_input.setObjectName("user_input")

        self.password_input = QtWidgets.QLineEdit(Form)
        self.password_input.setGeometry(QtCore.QRect(200, 260, 221, 31))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)  # Скрываем пароль
        self.password_input.setObjectName("password_input")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Log In"))
        self.Log_in_button.setText(_translate("Form", "Log in"))
        self.Captcha_button.setText(_translate("Form", "CAPTCHA"))
        self.New_user_button.setText(_translate("Form", "New user"))
        self.Password_label.setText(_translate("Form", "Password"))
        self.User_name_label.setText(_translate("Form", "User name"))

    def on_Log_in_button_clicked(self):
        name = self.user_input.text().strip()
        password = self.password_input.text().strip()

        if name in self.users and password == self.users[name].get_password():
            if self.ticket_window is None:
                self.ticket_window = QtWidgets.QWidget()
                self.ui_ticket = Ui_Form2()
                self.ui_ticket.setupUi(self.ticket_window)
            self.ui_ticket.user_status(name)
            self.ticket_window.show()
            
        else:
            print("Ошибка входа: неверное имя пользователя или пароль")
            
    def on_new_user_button_clicked(self):
        name = self.user_input.text().strip()
        password = self.password_input.text().strip()
        
        if name not in self.users:
            self.users[name]=Client(name,password)
        else:
            print("Error")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
