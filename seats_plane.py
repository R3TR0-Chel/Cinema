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
        
    def add_atriburs(self, user ,time,movie):
        # self.seats = data
        self.user = user
        self.time = time
        self.movie = movie

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1270, 720)

        # Adjust grid layout container size
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 30, 1170, 600))  # Updated dimensions
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Centered "Buy" button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(560, 630, 130, 60))  # Updated position
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect "Buy" Button Click Event
        self.pushButton.clicked.connect(self.buy_seats)

        # Seat Booking Setup
        self.seat_data_url = "https://aleck.pythonanywhere.com/seats"  # Example URL
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

    def generate_seats(self,seat_data):
        # Define the layout with empty spaces
        seat_layout = [
            [1] * 17,  # First row - 17 seats
            [1] * 17,  # Second row - 17 seats
            [1] * 17,  # Third row - 17 seats
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],  # Fourth row with gaps
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]   # Fifth row with gaps
        ]

        booked_seats = seat_data

        for row_idx, row in enumerate(seat_layout):
            for col_idx, seat in enumerate(row):
                if seat == 1:  # Seat exists at this position
                    seat_button = QPushButton()
                    seat_button.setFixedSize(40, 40)  # Square buttons
                    seat_button.setCheckable(True)
                    seat_button.setProperty("index",[row_idx,col_idx])
                    # Define base style for all buttons with rounded edges
                    base_style = """
                        QPushButton {
                            border-radius: 5px;  /* Slightly rounded corners */
                            border: none;
                            background-color: #5a5a5a;  /* Default available seats color (dark gray) */
                        }
                        QPushButton:disabled {
                            background-color: #d9534f;  /* Booked seats color (red) */
                        }
                        QPushButton#reserved_by_you{
                            background-color: green;  
                        }
                    """
                    # Identify if the seat is booked
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
                    background-color: #f0ad4e;  /* Selected seats color (orange) */
                    border-radius: 5px;  /* Slightly rounded corners */
                    border: none;
                }
            """)
            self.selected_seats.append(seat_button.property("index"))
        
        else:
            seat_button.setStyleSheet("""
                QPushButton {
                    background-color: #5a5a5a;  /* Available seats color (dark gray) */
                    border-radius: 5px;  /* Slightly rounded corners */
                    border: none;
                }
            """)
            self.selected_seats.remove(seat_button.property("index"))

    def buy_seats(self):
        request = requests.post("https://aleck.pythonanywhere.com/seats-buy", json={"username":self.user, "schedule":self.time, "movie":self.movie, "seats":self.selected_seats})
        print(request.json())
        self.fetch_seat_data()
        QMessageBox.information(None, "Purchase", "Seats purchased successfully!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = seating_plan()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
