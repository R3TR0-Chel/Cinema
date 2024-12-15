from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import requests

class Ui_NU_page(object):
    def setupUi(self, Log_in_page):
        self.nu_page = Log_in_page  # Сохраняем ссылку на форму как атрибут класса
        Log_in_page.setObjectName("Log_in_page")
        Log_in_page.resize(700, 730)
        Log_in_page.setFixedSize(700, 730)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        Log_in_page.setFont(font)
        Log_in_page.setStyleSheet(
            """
            #Log_in_page {
                background-image: url('./images/ackground.jpg');
                background-position: center;
                background-repeat: no-repeat;
            }
            """
        )
        self.title = QtWidgets.QLabel(Log_in_page)
        self.title.setGeometry(QtCore.QRect(220, 90, 251, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setStyleSheet("""
            QLabel {
                background-color: #f0ad4e;
                border: none;
                border-radius: 20px;
                color: white;
                font-size: 32px;
                font-weight: bold;
                padding: 10px;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
            }
        """)
        self.User_name_input = QtWidgets.QLineEdit(Log_in_page)
        self.User_name_input.setGeometry(QtCore.QRect(170, 290, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.User_name_input.setFont(font)
        self.User_name_input.setObjectName("User_name_input")
        self.User_name_input.setStyleSheet("""
    QLineEdit {
        background-color: rgba(0, 0, 0, 100);
        border: 2px solid white;
        border-radius: 20px;
        color: white;
        padding-left: 10px;
        font-size: 16px;
    }
    QLineEdit:focus {
        border: 2px solid #f0ad4e;
    }
""")
        self.name_input = QtWidgets.QLineEdit(Log_in_page)
        self.name_input.setGeometry(QtCore.QRect(170, 340, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.name_input.setFont(font)
        self.name_input.setObjectName("name_input")
        self.name_input.setStyleSheet("""
    QLineEdit {
        background-color: rgba(0, 0, 0, 100);
        border: 2px solid white;
        border-radius: 20px;
        color: white;
        padding-left: 10px;
        font-size: 16px;
    }
    QLineEdit:focus {
        border: 2px solid #f0ad4e;
    }
""")
        self.sign_in_button = QtWidgets.QPushButton(Log_in_page)
        self.sign_in_button.setGeometry(QtCore.QRect(260, 510, 175, 71))
        self.sign_in_button.setObjectName("sign_in_button")
        self.sign_in_button.clicked.connect(self.sing_in_clicked)
        self.sign_in_button.setStyleSheet("""
            QPushButton {
                background-color: #f0ad4e;
                border: none;
                border-radius: 20px;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
            }
            QPushButton:hover {
                background-color: #ffbf6e;
            }
            QPushButton:pressed {
                background-color: #d98a36;
            }
        """)
        self.verify_password_input = QtWidgets.QLineEdit(Log_in_page)
        self.verify_password_input.setGeometry(QtCore.QRect(170, 390, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.verify_password_input.setFont(font)
        self.verify_password_input.setObjectName("verify_password_input")
        self.verify_password_input.setStyleSheet("""
    QLineEdit {
        background-color: rgba(0, 0, 0, 100);
        border: 2px solid white;
        border-radius: 20px;
        color: white;
        padding-left: 10px;
        font-size: 16px;
    }
    QLineEdit:focus {
        border: 2px solid #f0ad4e;
    }
""")

        self.retranslateUi(Log_in_page)
        QtCore.QMetaObject.connectSlotsByName(Log_in_page)

    def retranslateUi(self, Log_in_page):
        _translate = QtCore.QCoreApplication.translate
        Log_in_page.setWindowTitle(_translate("Log_in_page", "Form"))
        self.title.setText(_translate("Log_in_page", "Moviepoint"))
        self.User_name_input.setPlaceholderText(_translate("Log_in_page", "Username"))
        self.name_input.setPlaceholderText(_translate("Log_in_page", "Name"))
        self.sign_in_button.setText(_translate("Log_in_page", "Sign in"))
        self.verify_password_input.setPlaceholderText(_translate("Log_in_page", "Password"))
        
    def sing_in_clicked(self):
        name = self.name_input.text().strip()
        user_name = self.User_name_input.text().strip()
        password = self.verify_password_input.text().strip()
        request = requests.post("http://aleck.pythonanywhere.com/registration", json={"name": name, "password": password, "username": user_name})
        if request.status_code == 201:
            print("Added")
            QMessageBox.information(None, "Registration", "New user added successfully!")
            if self.nu_page:  # Проверяем, существует ли форма
                self.nu_page.close()
        else:
            print("Error")
            QMessageBox.information(None, "Registration", "Error. Try again later.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nu_page = QtWidgets.QWidget()
    ui = Ui_NU_page()
    ui.setupUi(nu_page)
    nu_page.show()
    sys.exit(app.exec_())
