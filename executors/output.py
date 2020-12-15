from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QApplication


class OutputWindow(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setGeometry(0, QApplication.desktop().height() // 2,
                         QApplication.desktop().width(), 50)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 10, 10))
        self.label.setObjectName("label")
        self.label.setText(args[1])
        self.label.adjustSize()