from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5.QtWidgets import QComboBox


class Ui_Movie_report(object):
    def __init__(self):
        self.movie = None
        self.time = None
        self.movie_data = None

    def add_data(self, movie):
        self.movie = movie

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 800)
        Form.setFixedSize(750, 800)
        Form.setStyleSheet(
            """
            #Form {
                background-image: url('./images/ackground.jpg');
                background-position: center;
                background-repeat: no-repeat;
            }
            """
        )

        # Title (Logo) Outside the Frame
        self.logo_title = QtWidgets.QLabel(Form)
        self.logo_title.setGeometry(QtCore.QRect(200, 20, 350, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.logo_title.setFont(font)
        self.logo_title.setStyleSheet("color: orange;")
        self.logo_title.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_title.setObjectName("logo_title")

        # Frame for the Details
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(160, 100, 421, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("""\
            QFrame {
                background-color: rgba(200, 200, 200, 200); /* Light transparent background */
                border: 2px solid white; /* White border */
                border-radius: 15px; /* Rounded corners */
                color: black; /* Text color */
                font-size: 14px; /* Font size */
            }
        """)

        # Movie Title Section with ComboBox
        self.Movie_title = QtWidgets.QLabel(self.frame)
        self.Movie_title.setGeometry(QtCore.QRect(40, 50, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Movie_title.setFont(font)
        self.Movie_title.setObjectName("Movie_title")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(150, 50, 200, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged.connect(self.update_list_view)

        # Quantity Section
        self.quantity_title = QtWidgets.QLabel(self.frame)
        self.quantity_title.setGeometry(QtCore.QRect(40, 100, 100, 30))
        self.quantity_title.setFont(font)
        self.quantity_title.setObjectName("quantity_title")
        self.title_output_2 = QtWidgets.QLabel(self.frame)
        self.title_output_2.setGeometry(QtCore.QRect(150, 100, 200, 30))
        self.title_output_2.setFont(font)
        self.title_output_2.setObjectName("title_output_2")

        # Seats Section
        self.seat_label = QtWidgets.QLabel(self.frame)
        self.seat_label.setGeometry(QtCore.QRect(40, 150, 100, 30))
        self.seat_label.setFont(font)
        self.seat_label.setObjectName("seat_label")
        self.title_output_3 = QtWidgets.QLabel(self.frame)
        self.title_output_3.setGeometry(QtCore.QRect(150, 150, 200, 30))
        self.title_output_3.setFont(font)
        self.title_output_3.setObjectName("title_output_3")

        # People Section
        self.People_label = QtWidgets.QLabel(self.frame)
        self.People_label.setGeometry(QtCore.QRect(40, 200, 100, 30))
        self.People_label.setFont(font)
        self.People_label.setObjectName("People_label")

        # ListView Widget
        self.listView = QtWidgets.QListView(self.frame)
        self.listView.setGeometry(QtCore.QRect(40, 250, 341, 300))
        self.listView.setObjectName("listView")

        # Create the model for the ListView
        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def update_list_view(self):
        self.model.clear()
        quantity = 0
        for name, seats in self.movie_data["schedule"][self.comboBox.currentText()].items():
                list_item = QtGui.QStandardItem(name)
                self.model.appendRow(list_item)
                quantity += len(seats)
        self.title_output_2.setText(str(quantity))
        self.title_output_3.setText(str(81 - quantity))

    def update_combobox_with_movie_data(self):
        # Request data from the server
        print(self.movie)
        response = requests.get(f"http://aleck.pythonanywhere.com/movies-time?name={self.movie}")
        if response.status_code == 200:
             
            self.movie_data = response.json()
            print(self.movie_data)
            self.comboBox.clear()
            for item in self.movie_data.get('schedule', []).keys():
                self.comboBox.addItem(item)
            self.update_list_view()
            
        else:
            print("Failed to fetch movie data")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Movie Report"))
        self.logo_title.setText(_translate("Form", "Movie Point"))
        self.Movie_title.setText(_translate("Form", self.movie))
        self.quantity_title.setText(_translate("Form", "Quantity:"))
        self.title_output_2.setText(_translate("Form", "None"))
        self.seat_label.setText(_translate("Form", "Seats:"))
        self.title_output_3.setText(_translate("Form", "None"))
        self.People_label.setText(_translate("Form", "People:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Movie_report = QtWidgets.QWidget()
    ui = Ui_Movie_report()
    ui.setupUi(Movie_report)
    Movie_report.show()
    sys.exit(app.exec_())
