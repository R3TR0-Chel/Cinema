from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import requests

class Ui_NU_page(object):
    def setupUi(self, Log_in_page):
        Log_in_page.setObjectName("Log_in_page")
        Log_in_page.resize(700, 730)
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
        self.title.setAlignment(QtCore.Qt.AlignCenter)  # Выровнять текст по центру
        self.title.setStyleSheet("""
            QLabel {
                background-color: #f0ad4e; /* Оранжевый цвет */
                border: none;
                border-radius: 20px; /* Закругленные края */
                color: white;
                font-size: 32px; /* Увеличенный шрифт */
                font-weight: bold; /* Полужирный текст */
                padding: 10px; /* Отступы внутри кнопки */
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); /* Тень */
            }
            QPushButton:hover {
                background-color: #ffbf6e; /* Более светлый оранжевый при наведении */
            }
            QPushButton:pressed {
                background-color: #d98a36; /* Темный оранжевый при нажатии */
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
        background-color: rgba(0, 0, 0, 100); /* Прозрачный фон с черным оттенком */
        border: 2px solid white; /* Белая рамка */
        border-radius: 20px; /* Закругленные углы */
        color: white; /* Цвет текста */
        padding-left: 10px; /* Отступ для текста */
        font-size: 16px; /* Размер текста */
    }
    QLineEdit:focus {
        border: 2px solid #f0ad4e; /* Цвет рамки при фокусе */
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
        background-color: rgba(0, 0, 0, 100); /* Прозрачный фон с черным оттенком */
        border: 2px solid white; /* Белая рамка */
        border-radius: 20px; /* Закругленные углы */
        color: white; /* Цвет текста */
        padding-left: 10px; /* Отступ для текста */
        font-size: 16px; /* Размер текста */
    }
    QLineEdit:focus {
        border: 2px solid #f0ad4e; /* Цвет рамки при фокусе */
    }
""")
        self.sign_in_button = QtWidgets.QPushButton(Log_in_page)
        self.sign_in_button.setGeometry(QtCore.QRect(260, 510, 175, 71))
        self.sign_in_button.setObjectName("sign_in_button")
        self.sign_in_button.clicked.connect(self.sing_in_clicked)
        self.sign_in_button.setStyleSheet("""
            QPushButton {
                background-color: #f0ad4e; /* Оранжевый цвет */
                border: none;
                border-radius: 20px; /* Закругленные края */
                color: white;
                font-size: 18px; /* Увеличенный шрифт */
                font-weight: bold; /* Полужирный текст */
                padding: 10px; /* Отступы внутри кнопки */
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); /* Тень */
            }
            QPushButton:hover {
                background-color: #ffbf6e; /* Более светлый оранжевый при наведении */
            }
            QPushButton:pressed {
                background-color: #d98a36; /* Темный оранжевый при нажатии */
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
        background-color: rgba(0, 0, 0, 100); /* Прозрачный фон с черным оттенком */
        border: 2px solid white; /* Белая рамка */
        border-radius: 20px; /* Закругленные углы */
        color: white; /* Цвет текста */
        padding-left: 10px; /* Отступ для текста */
        font-size: 16px; /* Размер текста */
    }
    QLineEdit:focus {
        border: 2px solid #f0ad4e; /* Цвет рамки при фокусе */
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
        request = requests.post("http://aleck.pythonanywhere.com/registration", json={"name":name,"password":password,"username":user_name})
        if request.status_code == 201:
            print("Added")
            QMessageBox.information(None, "Purchase", "New user added successfully!")    
            nu_page.close()
        else:
            print("Error")
            QMessageBox.information(None, "Purchase", "Error try again later")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nu_page = QtWidgets.QWidget()
    ui = Ui_NU_page()
    ui.setupUi(nu_page)
    nu_page.show()
    sys.exit(app.exec_())
