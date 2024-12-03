from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QMessageBox,
)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class CinemaHall(QWidget):
    def __init__(self, rows=5, cols=8, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Кинозал")
        self.setGeometry(100, 100, 800, 600)

        # Хранилище статусов мест
        self.seats = {}
        self.selected_seat = None

        # Основной макет
        main_layout = QVBoxLayout(self)

        # Заголовок
        self.title_label = QLabel("Выберите место:", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.title_label)

        # Макет зала
        self.grid_layout = QGridLayout()
        main_layout.addLayout(self.grid_layout)

        # Кнопка бронирования
        self.book_button = QPushButton("Забронировать", self)
        self.book_button.clicked.connect(self.book_seat)
        main_layout.addWidget(self.book_button)

        # Создаем места
        self.create_seats(rows, cols)

    def create_seats(self, rows, cols):
        for row in range(rows):
            for col in range(cols):
                # Создаем кнопку для каждого места
                seat = QPushButton(f"{row + 1}-{col + 1}")
                seat.setStyleSheet("background-color: green; color: white;")
                seat.clicked.connect(lambda _, r=row, c=col: self.select_seat(r, c))
                self.grid_layout.addWidget(seat, row, col)

                # Сохраняем статус места
                self.seats[(row, col)] = {"status": "free", "button": seat}

    def select_seat(self, row, col):
        if self.selected_seat:
            # Сбрасываем предыдущий выбор
            r, c = self.selected_seat
            if self.seats[(r, c)]["status"] == "free":
                self.seats[(r, c)]["button"].setStyleSheet("background-color: green; color: white;")

        # Обновляем текущий выбор
        self.selected_seat = (row, col)
        seat_status = self.seats[(row, col)]["status"]

        if seat_status == "free":
            self.seats[(row, col)]["button"].setStyleSheet("background-color: yellow; color: black;")
        elif seat_status == "booked":
            QMessageBox.warning(self, "Ошибка", "Это место уже занято.")

    def book_seat(self):
        if not self.selected_seat:
            QMessageBox.warning(self, "Ошибка", "Выберите место для бронирования.")
            return

        row, col = self.selected_seat
        seat_status = self.seats[(row, col)]["status"]

        if seat_status == "free":
            self.seats[(row, col)]["status"] = "booked"
            self.seats[(row, col)]["button"].setStyleSheet("background-color: red; color: white;")
            self.selected_seat = None
            QMessageBox.information(self, "Успех", f"Место {row + 1}-{col + 1} забронировано.")
        else:
            QMessageBox.warning(self, "Ошибка", "Это место уже занято.")

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = CinemaHall(rows=6, cols=10)
    window.show()
    sys.exit(app.exec_())
