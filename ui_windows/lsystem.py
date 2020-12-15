from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindowLSystems(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 480)
        MainWindow.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 400, 201, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 204, 0);")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(400, 10, 231, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 204, 0);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "selection-color: rgb(100, 100, 100);\n"
                                    "selection-background-color: "
                                    "rgb(255, 255, 127);\n"
                                    "font: 12pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 381, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 400, 21, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 204, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "L-системы"))
        self.pushButton.setText(_translate("MainWindow", "Редактировать"))
        self.pushButton_2.setText(_translate("MainWindow", "←"))
