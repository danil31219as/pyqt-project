from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 480)
        MainWindow.setStyleSheet("color:rgb(255, 255, 255);\n"
                                 "background-color: "
                                 "qlineargradient(spread:pad, x1:0, y1:0, "
                                 "x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), "
                                 "stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 120, 191, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(255, 204, 0);\n"
                                      "border-color: rgb(0, 0, 0);\n"
                                      "font: italic 16pt "
                                      "\"Monotype Corsiva\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(255, 204, 0);\n"
                                        "font: italic 16pt "
                                        "\"Monotype Corsiva\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setStyleSheet(
            "font: italic 16pt \"Monotype Corsiva\";\n"
            "background-color: rgb(255, 204, 0);\n"
            "color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 0, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: italic 48pt \"Monotype Corsiva\";\n"
                                 "color: qlineargradient(spread:pad, "
                                 "x1:0, y1:0, x2:1, y2:0,"
                                 " stop:0 rgba(0, 0, 0, 255), "
                                 "stop:1 rgba(255, 255, 255, 255));\n"
                                 "background-color: "
                                 "qlineargradient(spread:pad, "
                                 "x1:0, y1:0, x2:1, y2:0, stop:0 "
                                 "rgba(0, 0, 0, 255), stop:1 "
                                 "rgba(255, 255, 255, 255));\n"
                                 "")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "L-systems"))
        self.pushButton_2.setText(_translate("MainWindow", "Уравнения"))
        self.pushButton_3.setText(_translate("MainWindow", "Помощь"))
        self.label.setText(_translate("MainWindow", "Матан"))
