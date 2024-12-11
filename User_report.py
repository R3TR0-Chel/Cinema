from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_User_report(object):
    def __init__(self,user):
        self.user = user
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
        self.title.setGeometry(QtCore.QRect(225, 50, 300, 90))
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
            }
           
        """)
        self.user_output = QtWidgets.QListView(Form)
        self.user_output.setGeometry(QtCore.QRect(170, 190, 400, 500))
        self.user_output.setObjectName("user_output")
        self.user_output.setStyleSheet("""
    QListView {
        background-color: rgba(200, 200, 200, 200); /* Прозрачный черный фон */
        border: 2px solid white; /* Белая рамка */
        border-radius: 15px; /* Закругленные углы */
        color: white; /* Цвет текста */
        font-size: 14px; /* Размер шрифта */
        padding: 5px; /* Внутренние отступы */
    }""")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "Moviepoint"))
        
    def user_history(self):
        responce = requests.get(f"http://aleck.pythonanywhere.com/watched?username={self.user}").json()
        self.model = QtGui.QStandardItemModel()
        print(responce)
        for item in responce["watched"]:
            self.model.appendRow(QtGui.QStandardItem(str(f"{item[0]} {item[1]}")))
        self.user_output.setModel(self.model)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    User_report = QtWidgets.QWidget()
    ui = Ui_User_report()
    ui.setupUi(User_report)
    User_report.show()
    sys.exit(app.exec_())

