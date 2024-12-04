from PyQt5 import QtCore, QtGui, QtWidgets
from Movies_class import movie

class Ui_Main_page(object):
    def __init__(self):
        self.user = None
        self.Movies_left = {
            "Gladiator II": "./images/ackground.jpg",
            "Moana 2": "./images/ackground.jpg",
            "Batman": "./images/ackground.jpg",
            "John Wick": "./images/ackground.jpg",
            "Inception": "./images/ackground.jpg"
        }
        self.Movies_right = {
            "Interstellar": "./images/ackground.jpg",
            "Spider-Man": "./images/ackground.jpg",
            "Avatar": "./images/ackground.jpg",
            "Kizumonogatari": "./images/ackground.jpg",
            "Weathering with You":"./images/ackground.jpg"
        }
        self.schedule_classes = {"Gladiator II":movie("Gladiator II",["12:00","14:00","17:00","20:30"],500),
                         "Moana 2":movie("Moana 2",["10:00","12:00","14:00","21:00"],450),
                         "Batman": movie("Batman",["20:00","21:00","22:00","23:30"],600),
                         "Interseallar":movie("Interstellar",["20:00","21:00"],500)
                         }
    
    def add_user(self,name):
        self.user = name
        print(self.user)

    def setupUi(self, Main_page):
        Main_page.setObjectName("Main_page")
        Main_page.resize(1270, 720)

        # Левый контейнер
        self.Left_container = QtWidgets.QWidget(Main_page)
        self.Left_container.setGeometry(QtCore.QRect(25, 65, 250, 600))
        self.Left_container.setObjectName("Left_container")
        
        # Создаем QScrollArea для левого контейнера
        self.Left_scroll_area = QtWidgets.QScrollArea(self.Left_container)
        self.Left_scroll_area.setGeometry(QtCore.QRect(0, 0, 250, 600))
        self.Left_scroll_area.setWidgetResizable(True)
        self.Left_scroll_area.setObjectName("Left_scroll_area")

        # Виджет для содержимого левого контейнера
        self.Left_content = QtWidgets.QWidget()
        self.Left_content.setObjectName("Left_content")
        self.Left_scroll_area.setWidget(self.Left_content)

        # Правый контейнер
        self.Right_container = QtWidgets.QWidget(Main_page)
        self.Right_container.setGeometry(QtCore.QRect(996, 65, 250, 600))
        self.Right_container.setObjectName("Right_container")
        
        # Создаем QScrollArea для правого контейнера
        self.Right_scroll_area = QtWidgets.QScrollArea(self.Right_container)
        self.Right_scroll_area.setGeometry(QtCore.QRect(0, 0, 250, 600))
        self.Right_scroll_area.setWidgetResizable(True)
        self.Right_scroll_area.setObjectName("Right_scroll_area")

        # Виджет для содержимого правого контейнера
        self.Right_content = QtWidgets.QWidget()
        self.Right_content.setObjectName("Right_content")
        self.Right_scroll_area.setWidget(self.Right_content)

        # Настройка шрифта заголовка
        self.Title = QtWidgets.QLabel(Main_page)
        self.Title.setGeometry(QtCore.QRect(520, 30, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")

        # Создание и настройка списка для фильмов
        self.frame = QtWidgets.QFrame(Main_page)
        self.frame.setGeometry(QtCore.QRect(350, 120, 600, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.Movie_list = QtWidgets.QListWidget(self.frame)
        self.Movie_list.setGeometry(QtCore.QRect(0, 0, 291, 301))
        self.Movie_list.setObjectName("Movie_list")
        self.Movie_list.addItems(self.schedule_classes.keys())
        self.Movie_list.itemClicked.connect(self.show_movies)
        
        self.Schedule_list = QtWidgets.QListWidget(self.frame)
        self.Schedule_list.setGeometry(QtCore.QRect(290, 0, 311, 301))
        self.Schedule_list.setObjectName("Schedule_list")

        # Добавляем постеры в контейнеры
        self.displayPosters()

        # Создание кнопок
        self.Buy_button = QtWidgets.QPushButton(Main_page)
        self.Buy_button.setGeometry(QtCore.QRect(550, 480, 180, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Buy_button.setFont(font)
        self.Buy_button.setObjectName("Buy_button")
        
        self.movie_info_button = QtWidgets.QPushButton(Main_page)
        self.movie_info_button.setGeometry(QtCore.QRect(550, 550, 180, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.movie_info_button.setFont(font)
        self.movie_info_button.setObjectName("movie_info_button")
        
        self.User_history_button = QtWidgets.QPushButton(Main_page)
        self.User_history_button.setGeometry(QtCore.QRect(550, 620, 180, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.User_history_button.setFont(font)
        self.User_history_button.setObjectName("User_history_button")

        self.retranslateUi(Main_page)
        QtCore.QMetaObject.connectSlotsByName(Main_page)

    def displayPosters(self):
        """Заполняем контейнеры постерами с увеличенными размерами."""
        # Левый контейнер
        left_layout = QtWidgets.QVBoxLayout(self.Left_content)
        for movie, poster_path in self.Movies_left.items():
            label = QtWidgets.QLabel(self.Left_content)
            pixmap = QtGui.QPixmap(poster_path)
            pixmap = pixmap.scaled(200, 300, QtCore.Qt.KeepAspectRatio)  # Увеличиваем размер до 200x300
            label.setPixmap(pixmap)
            left_layout.addWidget(label)

        # Правый контейнер
        right_layout = QtWidgets.QVBoxLayout(self.Right_content)
        for movie, poster_path in self.Movies_right.items():
            label = QtWidgets.QLabel(self.Right_content)
            pixmap = QtGui.QPixmap(poster_path)
            pixmap = pixmap.scaled(200, 300, QtCore.Qt.KeepAspectRatio)  # Увеличиваем размер до 200x300
            label.setPixmap(pixmap)
            right_layout.addWidget(label)
            
    def show_movies(self,item):
        movie_name = item.text()
        schedule = self.schedule_classes.get(movie_name, []) .get_schedule()
        self.Schedule_list.clear()
        self.Schedule_list.addItems(schedule)
        

    def retranslateUi(self, Main_page):
        _translate = QtCore.QCoreApplication.translate
        Main_page.setWindowTitle(_translate("Main_page", "Form"))
        self.Title.setText(_translate("Main_page", "Moviepoint"))
        self.Buy_button.setText(_translate("Main_page", "Buy"))
        self.movie_info_button.setText(_translate("Main_page", "Movie info"))
        self.User_history_button.setText(_translate("Main_page", "User history"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_page = QtWidgets.QWidget()
    ui = Ui_Main_page()
    ui.setupUi(Main_page)
    Main_page.show()
    sys.exit(app.exec_())
