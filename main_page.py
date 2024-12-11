from PyQt5 import QtCore, QtGui, QtWidgets
from Movies_class import movie
from seats_plane import seating_plan
import requests
from Movie_report import Ui_Movie_report
from User_report import Ui_User_report
class Ui_Main_page(object):
    def __init__(self):
        self.user = None
        self.Movies_left = {
            "Gladiator II": "./images/glad.jpg",
            "Moana 2": "./images/moana-2.jpeg",
            "Batman": "./images/bat.jpg",
            "John Wick": "./images/jw.webp",
            "Inception": "./images/inc.jpg"
        }
        self.Movies_right = {
            "Interstellar": "./images/int.jfif",
            "Spider-Man": "./images/sp.jpg",
            "Avatar": "./images/avatar.jpg",
            "Kizumonogatari": "./images/kizu.jpg",
            "Weathering with You":"./images/wwu.jpg"
        }
        self.seats_plan=None
        self.Mi=None
        self.Uinfo = None
    
    def add_user(self,name):
        self.user = name
        print(self.user)

    def setupUi(self, Main_page):
        Main_page.setObjectName("Main_page")
        Main_page.resize(1270, 720)
        Main_page.setStyleSheet(
            """
            #Main_page {
                background-image: url('./images/ackground.jpg');
                background-position: center;
                background-repeat: no-repeat;
            }
            """)
        
        request = requests.get("https://aleck.pythonanywhere.com/movies") 
        self.schedule_classes =request.json()

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
        self.Title.setGeometry(QtCore.QRect(490, 20, 300, 85))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Title.setStyleSheet("""
            QLabel {
                background-color: #f0ad4e; /* Оранжевый цвет */
                border: none;
                border-radius: 20px; /* Закругленные края */
                color: white;
                font-size: 32px; /* Увеличенный шрифт */
                font-weight: bold; /* Полужирный текст */
                padding: 10px; /* Отступы внутри кнопки */
            }
            QPushButton:hover {
                background-color: #ffbf6e; /* Более светлый оранжевый при наведении */
            }
            QPushButton:pressed {
                background-color: #d98a36; /* Темный оранжевый при нажатии */
            }
        """)
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
        self.Movie_list.setStyleSheet("""
    QListWidget {
        background-color: rgba(200, 200, 200, 200); /* Прозрачный черный фон */
        border: 2px solid white; /* Белая рамка */
        border-radius: 15px; /* Закругленные углы */
        color: white; /* Цвет текста */
        font-size: 14px; /* Размер шрифта */
        padding: 5px; /* Внутренние отступы */
    }
    QListWidget::item {
        background-color: rgba(50, 50, 50, 180); /* Светлый фон для элементов */
        border-radius: 10px; /* Закругленные элементы */
        margin: 5px; /* Отступы между элементами */
        padding: 5px;
    }
    QListWidget::item:hover {
        background-color: rgba(255, 255, 255, 60); /* Подсветка элемента при наведении */
        color: black
    }
    QListWidget::item:selected {
        background-color: #f0ad4e; /* Оранжевая подсветка выбранного элемента */
        color: black; /* Цвет текста выбранного элемента */
    }
""")      
        self.Schedule_list = QtWidgets.QListWidget(self.frame)
        self.Schedule_list.setGeometry(QtCore.QRect(290, 0, 311, 301))
        self.Schedule_list.setObjectName("Schedule_list")
        self.Schedule_list.setStyleSheet("""
    QListWidget {
        background-color: rgba(200, 200, 200, 200); /* Прозрачный черный фон */
        border: 2px solid white; /* Белая рамка */
        border-radius: 15px; /* Закругленные углы */
        color: white; /* Цвет текста */
        font-size: 14px; /* Размер шрифта */
        padding: 5px; /* Внутренние отступы */
    }
    QListWidget::item {
        background-color: rgba(50, 50, 50, 180); /* Светлый фон для элементов */
        border-radius: 10px; /* Закругленные элементы */
        margin: 5px; /* Отступы между элементами */
        padding: 5px;
    }
    QListWidget::item:hover {
        background-color: rgba(255, 255, 255, 60); /* Подсветка элемента при наведении */
        color: black
    }
    QListWidget::item:selected {
        background-color: #f0ad4e; /* Оранжевая подсветка выбранного элемента */
        color: black; /* Цвет текста выбранного элемента */
    }
""")
        # Добавляем постеры в контейнеры
        self.displayPosters()
        # Создание кнопок
        self.Buy_button = QtWidgets.QPushButton(Main_page)
        self.Buy_button.setGeometry(QtCore.QRect(550, 480, 180, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Buy_button.setFont(font)
        self.Buy_button.setObjectName("Buy_button")
        self.Buy_button.clicked.connect(self.buy_button_clicked)
        self.Buy_button.setStyleSheet("""
            QPushButton {
                background-color: #f0ad4e; /* Оранжевый цвет */
                border: none;
                border-radius: 20px; /* Закругленные края */
                color: white;
                font-size: 18px; /* Увеличенный шрифт */
                font-weight: bold; /* Полужирный текст */
                padding: 10px; /* Отступы внутри кнопки */
            }
            QPushButton:hover {
                background-color: #ffbf6e; /* Более светлый оранжевый при наведении */
            }
            QPushButton:pressed {
                background-color: #d98a36; /* Темный оранжевый при нажатии */
            }
        """)
        
        self.movie_info_button = QtWidgets.QPushButton(Main_page)
        self.movie_info_button.setGeometry(QtCore.QRect(550, 550, 180, 65))
        self.movie_info_button.clicked.connect(self.movie_info_buttton_clicked)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.movie_info_button.setFont(font)
        self.movie_info_button.setObjectName("movie_info_button")
        self.movie_info_button.setStyleSheet("""
            QPushButton {
                background-color: #f0ad4e; /* Оранжевый цвет */
                border: none;
                border-radius: 20px; /* Закругленные края */
                color: white;
                font-size: 18px; /* Увеличенный шрифт */
                font-weight: bold; /* Полужирный текст */
                padding: 10px; /* Отступы внутри кнопки */
            }
            QPushButton:hover {
                background-color: #ffbf6e; /* Более светлый оранжевый при наведении */
            }
            QPushButton:pressed {
                background-color: #d98a36; /* Темный оранжевый при нажатии */
            }
        """)
        
        self.User_history_button = QtWidgets.QPushButton(Main_page)
        self.User_history_button.setGeometry(QtCore.QRect(550, 620, 180, 65))
        self.User_history_button.clicked.connect(self.user_info_button_clicked)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.User_history_button.setFont(font)
        self.User_history_button.setObjectName("User_history_button")
        self.User_history_button.setStyleSheet("""
            QPushButton {
                background-color: #f0ad4e; /* Оранжевый цвет */
                border: none;
                border-radius: 20px; /* Закругленные края */
                color: white;
                font-size: 18px; /* Увеличенный шрифт */
                font-weight: bold; /* Полужирный текст */
                padding: 10px; /* Отступы внутри кнопки */
            }
            QPushButton:hover {
                background-color: #ffbf6e; /* Более светлый оранжевый при наведении */
            }
            QPushButton:pressed {
                background-color: #d98a36; /* Темный оранжевый при нажатии */
            }
        """)

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
        schedule = self.schedule_classes[movie_name]
        self.Schedule_list.clear()
        self.Schedule_list.addItems(schedule)
    
    def buy_button_clicked(self):
        time = self.Schedule_list.currentItem().text()
        movie = self.Movie_list.currentItem().text()
        if time and movie:
            if self.seats_plan is None:
                self.seats_plan = QtWidgets.QWidget()
                self.ui_seats = seating_plan()
                self.ui_seats.add_atriburs( self.user,time,movie)
                self.ui_seats.setupUi(self.seats_plan)
            else:
                self.ui_seats.add_atriburs( self.user, time,movie)
                print(self.ui_seats.movie,self.ui_seats.time)
                self.ui_seats.setupUi(self.seats_plan)
                print(True)
            self.seats_plan.show()
            
    def movie_info_buttton_clicked(self):
        movie = self.Movie_list.currentItem().text()
        if self.Mi is None:
            self.Mi = QtWidgets.QWidget()
            self.ui_mi=Ui_Movie_report()
            self.ui_mi.add_data(movie)
            self.ui_mi.setupUi(self.Mi)
            self.ui_mi.update_combobox_with_movie_data()
        else:
            self.Mi = QtWidgets.QWidget()
            self.ui_mi=Ui_Movie_report()
            self.ui_mi.add_data(movie)
            self.ui_mi.setupUi(self.Mi)
            self.ui_mi.update_combobox_with_movie_data()
        self.Mi.show()
    
    def user_info_button_clicked(self):
        if self.Uinfo is None:
            self.Uinfo = QtWidgets.QWidget()
            self.ui_Ui=Ui_User_report(self.user)
            self.ui_Ui.setupUi(self.Uinfo)
            self.ui_Ui.user_history()
        else:
            self.Uinfo = QtWidgets.QWidget()
            self.ui_Ui=Ui_User_report(self.user)
            self.ui_Ui.setupUi(self.Uinfo)
            self.ui_Ui.user_history()
        self.Uinfo.show()
        
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
