import os
import sqlite3
from math import cos, sin, pi

from PIL import Image, ImageDraw
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QColorDialog, \
    QInputDialog


from ui_windows.lsystem2 import UiFormLSystems2


class WindowLSystems2(UiFormLSystems2, QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.args = args
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setMinimum(1)
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.choose_color)
        self.pushButton_3.clicked.connect(self.choose_step)
        self.pushButton_4.clicked.connect(self.open_drawer)
        self.pushButton_5.clicked.connect(self.add_to_db)
        self.pushButton_6.clicked.connect(self.load_l_systems)
        self.pushButton_7.clicked.connect(self.return_window)
        self.pushButton_8.clicked.connect(self.choose_angle)
        self.pushButton_9.clicked.connect(self.save_item)
        self.pushButton_10.clicked.connect(self.del_item)
        self.pushButton_11.clicked.connect(self.choose_width)
        self.name = None
        self.angle = None
        self.axiom = None
        self.drawer = []
        self.mover = []
        self.plus_minus = None
        self.saver = []
        self.returner = []
        self.plus_180 = []
        self.rules = ''
        self.step = 10
        self.color = (0, 0, 0)
        self.stage = 1
        self.name_system = ''
        self.comboBox.addItem('')
        self.set_in_combobox()
        self.start_angle = 0
        self.width_draw = 1
        self.show()

    def open_file(self):  # вставить данные из файла
        filename = QFileDialog.getOpenFileName(self, 'Выбрать L-систему', '')[
            0]
        if filename:
            infile = open(filename).read().strip().split('\n')
            if infile:
                self.set_value_line(infile)

    def set_value_line(self, infile):
        name, angle, axiom, drawer, mover, plus_minus, \
        saver, returner, plus_180, rules = infile
        self.lineEdit.setText(str(name))
        self.lineEdit_2.setText(str(angle))
        self.lineEdit_3.setText(str(axiom))
        self.lineEdit_4.setText(str(drawer))
        self.lineEdit_5.setText(str(mover))
        self.lineEdit_6.setText(str(plus_minus))
        self.lineEdit_7.setText(str(saver))
        self.lineEdit_8.setText(str(returner))
        self.lineEdit_9.setText(str(plus_180))
        self.lineEdit_10.setText(str(rules))

    def choose_color(self):  # выбрать цвет
        self.color = QColorDialog.getColor().name()

    def choose_step(self):  # выбрать длину шага
        self.step = \
            QInputDialog.getInt(self, "", "Введите длину шага", self.step, 1,
                                20, 1)[0]

    def choose_angle(self):  # выбрать начальный угол
        self.start_angle = \
            QInputDialog.getInt(self, "", "Введите начальный угол",
                                self.start_angle, -180, 180, 1)[0]

    def choose_width(self):  # выбрать толщину линии
        self.width_draw = \
            QInputDialog.getInt(self, "", "Введите толщину линии",
                                self.width_draw, 1, 10, 1)[0]

    def set_in_combobox(self):  # установить значения в combobox
        con = sqlite3.connect('db/L_systems.db')
        cur = con.cursor()
        name_list = cur.execute(
            '''select name from draw_l_systems''').fetchall()
        for name in name_list:
            self.comboBox.addItem(name[0])
        con.close()

    def return_window(self):  # возвратиться в предыдущее окно
        self.close_window = self.args[-2](self, self.args[-7], self.args[-6], self.args[-5], self.args[-4], self.args[-3], self.args[-2] ,self.args[-1])
        self.close_window.show()
        self.close()

    def set_values(self):  # установить значения пременным
        self.name = self.lineEdit.text()
        self.angle = self.lineEdit_2.text()
        self.axiom = self.lineEdit_3.text()
        self.drawer = self.lineEdit_4.text()
        self.mover = self.lineEdit_5.text()
        self.plus_minus = self.lineEdit_6.text()
        self.saver = self.lineEdit_7.text()
        self.returner = self.lineEdit_8.text()
        self.plus_180 = self.lineEdit_9.text()
        self.rules = self.lineEdit_10.text()

    def load_l_systems(self):  # скачать данные о L-системе
        way_name, okBtnPressed = QInputDialog.getText(self, "Введите путь",
                                                      "Путь")
        if okBtnPressed:
            self.set_values()
            if self.name and self.axiom and self.angle and self.drawer and \
                    self.plus_minus and self.rules:
                if way_name:
                    way_name += f'''\{self.name}'''
                else:
                    way_name = f'''{self.name}'''
                self.draw_image(self.horizontalSlider.value(),
                                way_name + '.jpg')
                infile = open(way_name + '.txt', 'w')
                infile.write('\n'.join([self.name, str(self.angle), self.axiom,
                                        self.drawer, self.mover,
                                        self.plus_minus, self.saver,
                                        self.returner,
                                        self.plus_180, self.rules]))

    def del_item(self):  # удалить L-систему из базы данных
        self.set_values()
        if self.name:
            con = sqlite3.connect('db/L_systems.db')
            cur = con.cursor()
            cur.execute(
                f'''delete from draw_l_systems 
                where name = "{self.name}"''').fetchall()
            con.commit()
            con.close()

    def save_item(self):  # сохранить изменения
        self.set_values()
        binary = self.draw_image(3, self.name + '.jpg')
        os.remove(self.name + '.jpg')
        con = sqlite3.connect('db/L_systems.db')
        cur = con.cursor()
        cur.execute(f'''update draw_l_systems
                    set angle = {self.angle} 
AND axiom = "{self.axiom}" 
AND drawer = "{self.drawer}" 
AND mover = "{self.mover}" 
AND plus_minus = "{self.plus_minus}" 
AND saver = "{self.saver}" 
AND returner = "{self.returner}" 
AND plus_180 = "{self.plus_180}" 
AND rules = "{self.rules}" where name = "{self.name}"''')
        cur.execute(f'''update draw_l_systems
set image = ? where name = "{self.name}"''', (binary,))
        con.commit()
        con.close()

    def add_to_db(self):  # добавить L-систему в базу данных
        con = sqlite3.connect('db/L_systems.db')
        cur = con.cursor()
        self.set_values()
        if self.name and self.axiom and self.angle and self.drawer and \
                self.plus_minus and self.rules:
            binary = self.draw_image(3, f'{self.name}.jpg')
            os.remove(self.name + '.jpg')
            cur.execute(
                '''insert into draw_l_systems(name, angle, axiom, drawer, 
                mover, plus_minus, saver, returner, plus_180, rules, image)
                 values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (self.name, str(self.angle), self.axiom, self.drawer,
                 self.mover, self.plus_minus, self.saver, self.returner,
                 self.plus_180, self.rules, binary))
            con.commit()
            con.close()
            self.comboBox.addItem(self.name)
            con.close()

    def draw_image(self, n, way):  # нарисовать изображение для сохранения
        self.set_values()
        self.dict_rules = {}
        if self.angle:
            if self.angle.isascii():
                angle_new = float(self.angle)
            else:
                angle_new = None
        plus = None
        minus = None
        if self.rules:
            for elem in self.rules.split(','):
                elem = elem.strip().split()
                self.dict_rules[elem[0]] = elem[1]
        drawer = self.drawer.split()
        mover = self.mover.split()
        if self.plus_minus:
            plus, minus = self.plus_minus.split()
        saver = self.saver.split()
        returner = self.returner.split()
        plus_180 = self.plus_180.split()
        image = Image.new("RGB", (1080, 720), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        if angle_new and drawer and plus \
                and minus and self.rules and self.axiom:
            angle = self.start_angle
            x = 540
            y = 360
            coords = []
            axiom = self.red_rules(self.axiom, n)
            for rule in axiom:
                if rule in drawer:
                    draw.line((x, y, x + self.step * cos(
                        angle * pi / 180), y + self.step * sin(
                        angle * pi / 180)), fill=self.color,
                              width=self.width_draw)
                    x = x + self.step * cos(
                        angle * pi / 180)
                    y = y + self.step * sin(
                        angle * pi / 180)
                elif rule == plus:
                    angle += angle_new
                elif rule == minus:
                    angle -= angle_new
                elif rule in mover:
                    x = x + self.step * cos(
                        angle * pi / 180)
                    y = y + self.step * sin(
                        angle * pi / 180)
                elif rule in returner:
                    x, y, angle = coords.pop(- 1)
                elif rule in saver:
                    coords.append((x, y, angle))
                elif rule in plus_180:
                    angle += 180
            image.save(way)
            binary = sqlite3.Binary(open(self.name + '.jpg', 'rb').read())
            return binary

    def open_drawer(self):  # открыть окно для рисования
        self.stage = self.horizontalSlider.value()
        self.set_values()
        if self.angle and self.drawer and self.plus_minus \
                and self.rules and self.axiom:
            self.draw = self.args[-4](self, self.angle, self.axiom, self.drawer,
                               self.mover,
                               self.plus_minus, self.saver, self.returner,
                               self.plus_180,
                               self.rules, self.color, self.step,
                               self.stage,
                               self.start_angle, self.width_draw)
            self.draw.show()

    def paintEvent(self, event):  # для отслеживания добавлений в базу данных
        qp = QPainter()
        qp.begin(self)
        self.change_value()
        qp.end()

    def change_value(self):  # заполнение форм
        if self.comboBox.currentText():
            if self.comboBox.currentText() != self.name_system:
                self.name_system = self.comboBox.currentText()
                con = sqlite3.connect('db/L_systems.db')
                cur = con.cursor()
                infile = cur.execute(
                    f'''select name, angle, axiom, drawer, mover, 
                    plus_minus, saver, returner, plus_180, 
                    rules from draw_l_systems 
                    where name = "{self.name_system}"''').fetchall()[0]
                if infile:
                    name, angle, axiom, drawer, mover, plus_minus, saver, \
                    returner, plus_180, rules = infile
                    self.set_value_line(infile)
                con.close()

    def red_rules(self, axiom, n):  # редактирование правил для рисования
        for i in range(n):
            rules_res = ''
            for elem in axiom:
                if elem in self.dict_rules:
                    rules_res += self.dict_rules[elem]
                else:
                    rules_res += elem
            axiom = rules_res
        return axiom
