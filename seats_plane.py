import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton

class seating_plan(object):
    def __init__(self):
        self.movie = None
        self.time = None
        self.user = None
        self.selected_seats = []

    def add_atriburs(self, user, time, movie):
        self.user = user
        self.time = time
        self.movie = movie
        self.selected_seats = []  # Reset selected seats

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1270, 720)
        Form.setStyleSheet("""
            QPushButton {
                background-color: #d3d3d3;
                border: none;
                border-radius: 10px;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }
        """)

        # Adjust grid layout container size
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 30, 1170, 600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Centered "Buy" button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(560, 630, 130, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect "Buy" Button Click Event
        self.pushButton.clicked.connect(self.buy_seats)

        # Seat Booking Setup
        self.seat_data_url = "https://aleck.pythonanywhere.com/seats"
        self.fetch_seat_data()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Seat Booking"))
        self.pushButton.setText(_translate("Form", "Buy"))

    def fetch_seat_data(self):
        try:
            print(self.movie, self.time)
            response = requests.post(self.seat_data_url, json={"movie": self.movie, "schedule": self.time})
            response.raise_for_status()
            seat_data = response.json()
            self.generate_seats(seat_data)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(None, "Error", f"Failed to fetch seat data: {e}")

    def generate_seats(self, seat_data):
        # Define the layout with empty spaces
        seat_layout = [
            [1] * 17,
            [1] * 17,
            [1] * 17,
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
        ]

        booked_seats = seat_data

        for row_idx, row in enumerate(seat_layout):
            for col_idx, seat in enumerate(row):
                if seat == 1:  # Seat exists at this position
                    seat_button = QPushButton()
                    seat_button.setFixedSize(40, 40)
                    seat_button.setCheckable(True)
                    seat_button.setProperty("index", [row_idx, col_idx])

                    base_style = """
                        QPushButton {
                            border-radius: 5px;
                            border: none;
                            background-color: #d3d3d3;  /* Default available seats color (light gray) */
                        }
                        QPushButton:disabled {
                            background-color: #d9534f;
                        }
                        QPushButton#reserved_by_you {
                            background-color: green;
                        }
                    """

                    for user, seats in booked_seats["booked"].items():
                        if [row_idx, col_idx] in seats and self.user != user:
                            seat_button.setChecked(True)
                            seat_button.setEnabled(False)
                            seat_button.setStyleSheet(base_style)
                        elif [row_idx, col_idx] in seats and self.user == user:
                            seat_button.setChecked(True)
                            seat_button.setEnabled(False)
                            seat_button.setObjectName("reserved_by_you")
                            seat_button.setStyleSheet(base_style)
                        else:
                            seat_button.setStyleSheet(base_style)

                    seat_button.clicked.connect(lambda _, b=seat_button: self.handle_seat_selection(b))
                    self.gridLayout.addWidget(seat_button, row_idx, col_idx)

    def handle_seat_selection(self, seat_button):
        if seat_button.isChecked():
            seat_button.setStyleSheet("""
                QPushButton {
                    background-color: #f0ad4e;
                    border-radius: 5px;
                    border: none;
                }
            """)
            self.selected_seats.append(seat_button.property("index"))
        else:
            seat_button.setStyleSheet("""
                QPushButton {
                    background-color: #d3d3d3;
                    border-radius: 5px;
                    border: none;
                }
            """)
            self.selected_seats.remove(seat_button.property("index"))

    def buy_seats(self):
        print(self.selected_seats)
        request = requests.post("https://aleck.pythonanywhere.com/seats-buy", json={"username": self.user, "schedule": self.time, "movie": self.movie, "seats": self.selected_seats})
        print(request.json())
        self.fetch_seat_data()
        self.selected_seats = []
        QMessageBox.information(None, "Purchase", "Seats purchased successfully!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = seating_plan()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
