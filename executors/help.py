from PyQt5.QtWidgets import QMainWindow

from ui_windows.help import UiMainWindowHelp


class Helper(UiMainWindowHelp, QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.args = args
        self.setupUi(self)
        self.pushButton.clicked.connect(self.return_window)

    def return_window(self):  # вернуться в предыдущее окно
        self.start = self.args[-7](self, self.args[-7], self.args[-6], self.args[-5], self.args[-4], self.args[-3], self.args[-2], self.args[-1])
        self.start.show()
        self.close()