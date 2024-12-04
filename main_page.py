from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_page(object):
    def __init__(self):
        self.user = None
        self.Movies = {}
    def setupUi(self, Main_page):
        Main_page.setObjectName("Main_page")
        Main_page.resize(1270, 720)
        self.Left_posters = QtWidgets.QTableWidget(Main_page)
        self.Left_posters.setGeometry(QtCore.QRect(25, 65, 250, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Left_posters.sizePolicy().hasHeightForWidth())
        self.Left_posters.setSizePolicy(sizePolicy)
        self.Left_posters.setObjectName("Left_posters")
        self.Left_posters.setColumnCount(0)
        self.Left_posters.setRowCount(0)
        self.Rihgt_posters = QtWidgets.QTableWidget(Main_page)
        self.Rihgt_posters.setGeometry(QtCore.QRect(996, 65, 250, 600))
        self.Rihgt_posters.setObjectName("Rihgt_posters")
        self.Rihgt_posters.setColumnCount(0)
        self.Rihgt_posters.setRowCount(0)
        self.Title = QtWidgets.QLabel(Main_page)
        self.Title.setGeometry(QtCore.QRect(520, 30, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.frame = QtWidgets.QFrame(Main_page)
        self.frame.setGeometry(QtCore.QRect(350, 120, 600, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Movie_list = QtWidgets.QListWidget(self.frame)
        self.Movie_list.setGeometry(QtCore.QRect(0, 0, 291, 301))
        self.Movie_list.setObjectName("Movie_list")
        self.Schedule_list = QtWidgets.QListWidget(self.frame)
        self.Schedule_list.setGeometry(QtCore.QRect(290, 0, 311, 301))
        self.Schedule_list.setObjectName("Schedule_list")
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
