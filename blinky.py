import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 500, 300))
        self.label.setMinimumSize(QtCore.QSize(500, 300))
        self.label.setMaximumSize(QtCore.QSize(500, 300))
        self.label.setObjectName("label")

        # add label to main window
        MainWindow.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QMovie("giphy.gif")
        self.label.setMovie(self.movie)
        self.movie.start()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.show()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    timer = QtCore.QTimer()
    timer.singleShot(3000, QtWidgets.QApplication.instance().quit)
    sys.exit(app.exec_())


