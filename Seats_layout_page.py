import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton


class Ui_Form(object):
    def __init__(self):
        self.movie = "Interstellar"
        self.time = "20:00"
        self.user = "admin"
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1270, 720)
        
        # Existing Widgets and Layouts
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(69, 30, 561, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 380, 94, 30))  # Centered button
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect "Buy" Button Click Event
        self.pushButton.clicked.connect(self.buy_seats)

        # Seat Booking Setup
        self.seat_data_url = "http://aleck.pythonanywhere.com/seats"  # Example URL
        self.fetch_seat_data()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Buy"))

    def fetch_seat_data(self):
        try:
            response = requests.post(self.seat_data_url, json={"movie": self.movie, "schedule":self.time, "username":self.user})
            response.raise_for_status()
            seat_data = response.json()
            self.generate_seats(seat_data)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(None, "Error", f"Failed to fetch seat data: {e}")

    def generate_seats(self, seat_data):
        # Define the layout with empty spaces
        seat_layout = [
            [1] * 17,  # First row - 17 seats
            [1] * 17,  # Second row - 17 seats
            [1] * 17,  # Third row - 17 seats
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],  # Fourth row with gaps
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]   # Fifth row with gaps
        ]

        booked_seats = seat_data.get("booked", [])

        for row_idx, row in enumerate(seat_layout):
            for col_idx, seat in enumerate(row):
                if seat == 1:  # Seat exists at this position
                    seat_button = QPushButton()
                    seat_button.setFixedSize(40, 40)
                    seat_button.setCheckable(True)

                    # Define base style for all buttons with background color
                    base_style = """
                        QPushButton {
                            border-radius: 20px;
                            border: none;
                            background-color: #5a5a5a;  /* Default available seats color (dark gray) */
                        }
                        QPushButton:disabled {
                            background-color: #d9534f;  /* Booked seats color (red) */
                        }
                    """

                    # Identify if the seat is booked
                    if [row_idx, col_idx] in booked_seats:
                        seat_button.setChecked(True)
                        seat_button.setEnabled(False)
                        seat_button.setStyleSheet(base_style)
                    else:
                        seat_button.setStyleSheet(base_style)  # Available seats color (dark gray)

                    seat_button.clicked.connect(lambda _, b=seat_button: self.handle_seat_selection(b))
                    self.gridLayout.addWidget(seat_button, row_idx, col_idx)

    def handle_seat_selection(self,seat_button):
        if seat_button.isChecked():
            seat_button.setStyleSheet("""
                QPushButton {
                    background-color: #f0ad4e;  /* Selected seats color (orange) */
                    border-radius: 20px;
                    border: none;
                }
            """)
        else:
            seat_button.setStyleSheet("""
                QPushButton {
                    background-color: #5a5a5a;  /* Available seats color (dark gray) */
                    border-radius: 20px;
                    border: none;
                }
            """)

    def buy_seats(self):
        QMessageBox.information(None, "Purchase", "Seats purchased successfully!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
