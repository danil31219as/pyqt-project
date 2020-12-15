from PyQt5.QtWidgets import QMainWindow

from ui_windows.main_ui import UiMainWindow


class StartWindow(UiMainWindow, QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.args = args
        self.setupUi(self)
        self.setWindowTitle('Добро пожаловать')

        self.pushButton.clicked.connect(self.open_l_systems)
        self.pushButton_2.clicked.connect(self.open_equalation)
        self.pushButton_3.clicked.connect(self.open_helper)

    def open_l_systems(self):  # открытие формы с L_системами
        self.second_form = self.args[-2](self, self.args[-7], self.args[-6], self.args[-5], self.args[-4], self.args[-3], self.args[-2] ,self.args[-1])
        self.second_form.show()
        self.close()

    def open_equalation(self):  # открытие фомы с уравнениями
        self.equal_form = self.args[-5](self, self.args[-7], self.args[-6], self.args[-5], self.args[-4], self.args[-3], self.args[-2] ,self.args[-1])
        self.equal_form.show()
        self.close()

    def open_helper(self):
        self.help = self.args[-6](self, self.args[-7], self.args[-6], self.args[-5], self.args[-4], self.args[-3], self.args[-2] ,self.args[-1])
        self.help.show()
        self.close()