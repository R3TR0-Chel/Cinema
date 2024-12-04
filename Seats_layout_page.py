import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QLabel, QMessageBox, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt

class SeatBookingApp(QWidget):
    def __init__(self, seat_data_url):
        super().__init__()
        self.setWindowTitle("Seat Booking Plan")
        self.setStyleSheet("background-color: #ffffff;")
        self.seat_data_url = seat_data_url
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Seats plan for booking")
        title_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(title_label)

        # Grid Layout for Seats
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10)  # Add spacing between seats
        seat_frame = QFrame()
        seat_frame.setLayout(self.grid_layout)
        main_layout.addWidget(seat_frame)

        # Fetch seat data and generate the seats
        self.fetch_seat_data()

        # Divider Line
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(divider)

        # Bottom layout for the booking button
        button_layout = QHBoxLayout()
        book_button = QPushButton("Book Selected Seats")
        book_button.setStyleSheet("""
            QPushButton {
                background-color: orange;
                padding: 10px;
                border-radius: 10px;
                border: none;
            }
        """)
        button_layout.addStretch()
        button_layout.addWidget(book_button)
        button_layout.addStretch()
        main_layout.addLayout(button_layout)

        # Set main layout
        self.setLayout(main_layout)

    def fetch_seat_data(self):
        try:
            response = requests.get(self.seat_data_url)
            response.raise_for_status()
            seat_data = response.json()
            self.generate_seats(seat_data)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to fetch seat data: {e}")

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
                            border-radius: 10px;
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

                    seat_button.clicked.connect(self.handle_seat_selection)
                    self.grid_layout.addWidget(seat_button, row_idx, col_idx)

    def handle_seat_selection(self):
        seat_button = self.sender()
        if seat_button.isChecked():
            seat_button.setStyleSheet("""
                QPushButton {
                    background-color: #f0ad4e;  /* Selected seats color (orange) */
                    border-radius: 10px;
                    border: none;
                }
            """)
        else:
            seat_button.setStyleSheet("""
                QPushButton {
                    background-color: #5a5a5a;  /* Available seats color (dark gray) */
                    border-radius: 10px;
                    border: none;
                }
            """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    seat_data_url = "http://aleck.pythonanywhere.com/seats"  
    main_window = SeatBookingApp(seat_data_url)
    main_window.resize(800, 500)
    main_window.show()

    sys.exit(app.exec_())
