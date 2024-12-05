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
        self.title.setGeometry(QtCore.QRect(210, 90, 300, 90))  # Увеличиваем размер QLabel
        font = QtGui.QFont()
        font.setPointSize(46)  # Увеличиваем размер шрифта
        font.setBold(True)  # Делаем текст жирным
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
           
        """)
        
        self.User_name_input = QtWidgets.QLineEdit(Log_in_page)
        self.User_name_input.setGeometry(QtCore.QRect(170, 270, 371, 41))
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
        self.Password_input = QtWidgets.QLineEdit(Log_in_page)
        self.Password_input.setGeometry(QtCore.QRect(170, 340, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Password_input.setFont(font)
        self.Password_input.setObjectName("Password_input")
        self.Password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_input.setStyleSheet("""
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
        self.Log_in_button = QtWidgets.QPushButton(Log_in_page)
        self.Log_in_button.setGeometry(QtCore.QRect(260, 430, 175, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Log_in_button.setFont(font)
        self.Log_in_button.setObjectName("Log_in_button")
        self.Log_in_button.clicked.connect(self.Login_button_clicked)
        self.Log_in_button.setStyleSheet("""
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
        self.CAPTCHA_button = QtWidgets.QPushButton(Log_in_page)
        self.CAPTCHA_button.setGeometry(QtCore.QRect(260, 520, 175, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CAPTCHA_button.setFont(font)
        self.CAPTCHA_button.setObjectName("CAPTCHA_button")
        self.CAPTCHA_button.setStyleSheet("""
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
        self.New_user_button = QtWidgets.QPushButton(Log_in_page)
        self.New_user_button.setGeometry(QtCore.QRect(260, 610, 175, 71))
        self.New_user_button.setObjectName("New_user_button")
        self.New_user_button.clicked.connect(self.nu_button_clikced)
        self.New_user_button.setStyleSheet("""
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
