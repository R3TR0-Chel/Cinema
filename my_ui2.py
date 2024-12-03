from PyQt5 import QtCore, QtGui, QtWidgets
from Movie_class import Movie
from my_ui3 import Ui_Form3


class Ui_Form2(object):
    def __init__(self):
        self.user = None
        self.movies = {
            "Inception": Movie("Inception", ["12:30", "14:30", "16:00", "18:00"], 500),
            "Interstellar": Movie("Interstellar", ["8:00", "10:30", "13:00", "15:00"], 500),
            "Tenet": Movie("Tenet", ["21:00", "23:00"], 500),
            "Drive": Movie("Drive", ["12:00", "14:00", "15:00", "17:00"], 600),
        }
        self.ticket_ids = {}
        self.user_history=[]
        self.report = {}
        
    def user_status(self,user_name):
        self.user = user_name
        print(self.user)
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(646, 859)

        Form2.setStyleSheet(
    """
    #Form2 {
        background-image: url("./images/ackground.jpg");
        background-position: center;
        background-repeat: no-repeat;
    }
    """
)


        self.Buy_button = QtWidgets.QPushButton(Form2)
        self.Buy_button.setGeometry(QtCore.QRect(240, 560, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Buy_button.setFont(font)
        self.Buy_button.setObjectName("Buy_button")

        self.Movie_info_button = QtWidgets.QPushButton(Form2)
        self.Movie_info_button.setGeometry(QtCore.QRect(240, 640, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Movie_info_button.setFont(font)
        self.Movie_info_button.setObjectName("Movie_info_button")
        self.Movie_info_button.clicked.connect(self.on_movie_info_button_clicked)
        self.User_history_button = QtWidgets.QPushButton(Form2)
        self.User_history_button.setGeometry(QtCore.QRect(240, 720, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.User_history_button.setFont(font)
        self.User_history_button.setObjectName("User_history_button")

        self.Movie_list = QtWidgets.QListWidget(Form2)
        self.Movie_list.setGeometry(QtCore.QRect(50, 20, 256, 511))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Movie_list.setFont(font)
        self.Movie_list.setObjectName("Movie_list")
        self.Movie_list.addItems(self.movies.keys())
        self.Movie_list.itemClicked.connect(self.display_schedule)
        self.Schedule_list = QtWidgets.QListWidget(Form2)
        self.Schedule_list.setGeometry(QtCore.QRect(340, 20, 256, 511))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Schedule_list.setFont(font)
        self.Schedule_list.setObjectName("Schedule_list")
        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def display_schedule(self, item):
        movie_name = item.text()
        schedule = self.movies.get(movie_name, [])
        self.Schedule_list.clear()
        self.Schedule_list.addItems(schedule.get_schedule())
        
    def on_movie_info_button_clicked(self):
        movie_name = self.Movie_list.currentItem()
        if movie_name:
          self.report_window = QtWidgets.QWidget()
          self.ui_report = Ui_Form3()
          self.ui_report.setupUi(self.report_window)
          self.ui_report.movie_label.setText(movie_name.text())
          self.report_window.show()
        else:
            print('1')
        

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Form"))
        self.Buy_button.setText(_translate("Form2", "Buy"))
        self.Movie_info_button.setText(_translate("Form2", "Movie info"))
        self.User_history_button.setText(_translate("Form2", "User history"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form2 = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form2)
    Form2.show()
    sys.exit(app.exec_())
