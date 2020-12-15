from random import choice

from PyQt5.QtWidgets import QMainWindow, QInputDialog
from numpy import roots

from ui_windows.equalation import UiMainWindowEqualation


class Equalation(UiMainWindowEqualation, QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.args = args[1:]
        self.setupUi(self)
        self.range_start, self.range_end = (0, 100)
        self.pushButton.clicked.connect(self.solver)
        self.pushButton_2.clicked.connect(self.return_window)
        self.pushButton_3.clicked.connect(self.float_equalation)
        self.return_start = None

    def return_window(self):  # вернуть предыдущее окно
        self.return_start = self.args[-7](self, self.args[-7], self.args[-6], self.args[-5], self.args[-4], self.args[-3], self.args[-2] ,self.args[-1])
        self.return_start.show()
        self.close()

    def solver(self):  # решить уравнение
        equal = self.lineEdit.text()
        if equal and '=' in equal:
            variable = None
            if '^' in equal:
                equal = equal.replace('^', '**')
            equal = equal.split('=')
            equal = '(' + equal[0] + ') - (' + equal[1] + ')'
            for sign in equal:
                if sign.isalpha():
                    variable = sign
                    break
            x_coords = []
            y_coords = []
            roots = []
            if self.lineEdit_2.text():
                self.range_start = int(self.lineEdit_2.text())
            if self.lineEdit_3.text():
                self.range_end = int(self.lineEdit_3.text())
            for i in range(self.range_start, self.range_end + 1):
                x_coords.append(i)
                if i < 0:
                    replacer = '(' + str(i) + ')'
                else:
                    replacer = str(i)
                result = eval(equal.replace(variable, replacer))
                y_coords.append(result)
                if result == 0:
                    roots.append(str(i))
            self.graphicsView.clear()
            self.graphicsView.plot(x_coords, y_coords,
                                   pen=choice(('r', 'g', 'b', 'w', 'y')))

            if roots:
                self.label_2.setText('; '.join(roots))
            else:
                self.label_2.setText('нет')

    def float_equalation(self):  # посчитать нецелые корни
        koef, okBtnPressed = QInputDialog.getText(self, "Введите коэффициенты",
                                                  "Введите коэффициенты в "
                                                  "порядке убывания степени "
                                                  "уравнения вида f(x)=0")
        output = roots(list(map(int, koef.split())))
        output = list(map(str, output))
        self.output = self.args[-3](self, '; '.join(output), self.args[-7], self.args[-6], self.args[-5], self.args[-4], self.args[-3], self.args[-2] ,self.args[-1])
        self.output.show()