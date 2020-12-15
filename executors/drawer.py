from math import cos, sin, pi

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication


class Drawer(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()
        self.dict_rules = {}
        if args[1]:
            if args[1].isascii():
                self.angle = float(args[1])
            else:
                self.angle = None
        self.axiom = args[2]
        self.drawer = args[3]
        self.mover = args[4]
        self.plus = None
        self.minus = None
        self.plus_minus = args[5]
        self.saver = args[6]
        self.returner = args[7]
        self.plus_180 = args[8]
        self.rules = args[9]
        if self.rules:
            for elem in self.rules.split(','):
                elem = elem.strip().split()
                self.dict_rules[elem[0]] = elem[1]
        self.drawer = self.drawer.split()
        self.mover = self.mover.split()
        if self.plus_minus:
            self.plus, self.minus = self.plus_minus.split()
        self.saver = self.saver.split()
        self.returner = self.returner.split()
        self.plus_180 = self.plus_180.split()
        self.draw = False

        if type(args[10]).__name__ == 'tuple':
            self.color = QColor(0, 0, 0)
        else:
            self.color = QColor(args[10])
        self.stage = args[12]
        self.step = args[11]
        self.start_angle = args[13]
        self.width_draw = args[14]

    def initUI(self):
        self.setGeometry(0, 0, 1600, 800)
        w, h = QApplication.desktop().width(), QApplication.desktop().height()
        self.resize(int(w), int(h))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, h - 100, 91, 16))
        self.label.setObjectName("label")
        self.label.setText('Левая кнопка - установить начальную точку, '
                           'правая кнопка - увеличть этап эволюции, '
                           'колесо - увеличить/уменьшить начальный угол,'
                           ' W - увелить толщину, S - уменьшить толщину,'
                           ' A - уменьшить длину, D - увеличить длину')
        self.label.adjustSize()
        self.setStyleSheet('background-color: #ffffff')
        self.setWindowTitle('Рисование')

    def paintEvent(self, event):  # отслеживание действий пользователя
        qp = QPainter()
        qp.begin(self)
        self.draw_l_system(qp)
        qp.end()

    def mousePressEvent(self, event):  # функции нажатия мыши
        if (event.button() == Qt.LeftButton):
            self.draw = True
            self.x, self.y = event.x(), event.y()
        if (event.button() == Qt.RightButton):
            self.stage += 1

    def wheelEvent(self, event):  # функции вращения колесика
        if event.angleDelta().y() > 0:
            self.start_angle -= 1
        elif event.angleDelta().y() < 0:
            self.start_angle += 1
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.width_draw += 1
        if event.key() == Qt.Key_S:
            if self.width_draw > 1:
                self.width_draw -= 1
        if event.key() == Qt.Key_A:
            if self.step > 1:
                self.step -= 1
        if event.key() == Qt.Key_D:
            self.step += 1

    def draw_l_system(self, qp):  # рисование
        if self.draw and self.angle and self.drawer and self.plus \
                and self.minus and self.rules and self.axiom:
            angle = self.start_angle
            x = self.x
            y = self.y
            coords = []
            axiom = self.red_rules(self.axiom, self.stage)
            pen = QPen(self.color)
            pen.setWidth(self.width_draw)
            qp.setPen(pen)

            for rule in axiom:
                if rule in self.drawer:
                    qp.drawLine(x, y, x + self.step * cos(
                        angle * pi / 180), y + self.step * sin(
                        angle * pi / 180))
                    x = x + self.step * cos(
                        angle * pi / 180)
                    y = y + self.step * sin(
                        angle * pi / 180)
                elif rule == self.plus:
                    angle += self.angle
                elif rule == self.minus:
                    angle -= self.angle
                elif rule in self.mover:
                    x = x + self.step * cos(
                        angle * pi / 180)
                    y = y + self.step * sin(
                        angle * pi / 180)
                elif rule in self.returner:
                    x, y, angle = coords.pop(- 1)
                elif rule in self.saver:
                    coords.append((x, y, angle))
                elif rule in self.plus_180:
                    angle += 180
        self.update()

    def red_rules(self, axiom, n):  # редактирование правил рисования
        for i in range(n):
            rules_res = ''
            for elem in axiom:
                if elem in self.dict_rules:
                    rules_res += self.dict_rules[elem]
                else:
                    rules_res += elem
            axiom = rules_res
        return axiom
