from PyQt5 import QtCore, QtGui, QtWidgets
from main_page import Ui_Main_page
from NU_user_page import Ui_NU_page
import requests

class Ui_Log_in_page(object):
    def __init__(self):
        self.main_page = None
        self.nu_page = None
        
    def setupUi(self, Log_in_page):
        Log_in_page.setObjectName("Log_in_page")
        Log_in_page.resize(700, 730)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        Log_in_page.setFont(font)
        self.title = QtWidgets.QLabel(Log_in_page)
        self.title.setGeometry(QtCore.QRect(220, 90, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.User_name_input = QtWidgets.QLineEdit(Log_in_page)
        self.User_name_input.setGeometry(QtCore.QRect(170, 270, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.User_name_input.setFont(font)
        self.User_name_input.setObjectName("User_name_input")
        self.Password_input = QtWidgets.QLineEdit(Log_in_page)
        self.Password_input.setGeometry(QtCore.QRect(170, 340, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Password_input.setFont(font)
        self.Password_input.setObjectName("Password_input")
        self.Password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Log_in_button = QtWidgets.QPushButton(Log_in_page)
        self.Log_in_button.setGeometry(QtCore.QRect(260, 430, 175, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Log_in_button.setFont(font)
        self.Log_in_button.setObjectName("Log_in_button")
        self.Log_in_button.clicked.connect(self.Login_button_clicked)
        self.CAPTCHA_button = QtWidgets.QPushButton(Log_in_page)
        self.CAPTCHA_button.setGeometry(QtCore.QRect(260, 520, 175, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CAPTCHA_button.setFont(font)
        self.CAPTCHA_button.setObjectName("CAPTCHA_button")
        self.New_user_button = QtWidgets.QPushButton(Log_in_page)
        self.New_user_button.setGeometry(QtCore.QRect(260, 610, 175, 71))
        self.New_user_button.setObjectName("New_user_button")
        self.New_user_button.clicked.connect(self.nu_button_clikced)

        self.retranslateUi(Log_in_page)
        QtCore.QMetaObject.connectSlotsByName(Log_in_page)

    def retranslateUi(self, Log_in_page):
        _translate = QtCore.QCoreApplication.translate
        Log_in_page.setWindowTitle(_translate("Log_in_page", "Form"))
        self.title.setText(_translate("Log_in_page", "Moviepoint"))
        self.User_name_input.setPlaceholderText(_translate("Log_in_page", "Username"))
        self.Password_input.setPlaceholderText(_translate("Log_in_page", "Password"))
        self.Log_in_button.setText(_translate("Log_in_page", "Log in"))
        self.CAPTCHA_button.setText(_translate("Log_in_page", "CAPTCHA"))
        self.New_user_button.setText(_translate("Log_in_page", "New user"))
        
    def Login_button_clicked(self):
        name = self.User_name_input.text().strip()
        password = self.Password_input.text().strip()
        request = requests.post("http://aleck.pythonanywhere.com/login", json={"username":name,"password":password})
        print(request.status_code)
        if request.status_code == 200:
            if self.main_page is None:
                self.main_page = QtWidgets.QWidget()
                self.ui_main_page = Ui_Main_page()
                self.ui_main_page.setupUi(self.main_page)
            self.ui_main_page.add_user(name)
            self.main_page.show()
            Log_in_page.close()
        else:
            print("Error")
            
    def nu_button_clikced(self):
        if self.nu_page is None:
            self.nu_page = QtWidgets.QWidget()
            self.ui_nu_page = Ui_NU_page()
            self.ui_nu_page.setupUi(self.nu_page)
        self.nu_page.show()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Log_in_page = QtWidgets.QWidget()
    ui = Ui_Log_in_page()
    ui.setupUi(Log_in_page)
    Log_in_page.show()
    sys.exit(app.exec_())
