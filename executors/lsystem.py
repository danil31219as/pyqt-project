import sqlite3

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


from ui_windows.lsystem import UiMainWindowLSystems


class WindowLSystems(UiMainWindowLSystems, QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.args = args
        self.comboBox.addItem('')
        self.name_image = self.comboBox.currentText()
        self.pushButton.clicked.connect(self.open_second_l_systems)
        self.pushButton_2.clicked.connect(self.return_start_window)
        try:
            self.comboBox.view().pressed.connect(self.filter_table)
        except Exception as e:
            print(e)
        self.update_table()
        self.set_in_combobox()

    def set_in_combobox(self):  # загрузка данных в combobox
        con = sqlite3.connect('db/L_systems.db')
        cur = con.cursor()
        name_list = cur.execute(
            '''select name from draw_l_systems''').fetchall()
        for name in name_list:
            self.comboBox.addItem(name[0])
        con.close()

    def return_start_window(self):  # вернуться в предыдущее окно
        try:
            self.start = self.args[-7](self, self.args[-7], self.args[-6], self.args[-5], self.args[-4], self.args[-3], self.args[-2] ,self.args[-1])
            self.start.show()
            self.close()
        except Exception as e:
            print(e)

    def open_second_l_systems(self):  # открыть следующую форму
        self.open_2 = self.args[-1](self, self.args[-7], self.args[-6], self.args[-5], self.args[-4], self.args[-3], self.args[-2] ,self.args[-1])
        self.open_2.show()
        self.close()

    def update_table(self, search=''):  # обновить данные таблицы
        con = sqlite3.connect('db/L_systems.db')
        cur = con.cursor()
        head = [x[1] for x in cur.execute(
            """PRAGMA table_info(draw_l_systems)""").fetchall()]
        if search:
            table_values = cur.execute(
                f'''select id, name, angle, axiom, drawer, mover, 
                plus_minus, saver, returner, plus_180, 
                rules, image from draw_l_systems WHERE name = "{search}"''').fetchall()
        else:
            table_values = cur.execute(
                '''select id, name, angle, axiom, drawer, mover, 
                plus_minus, saver, returner, plus_180, 
                rules, image from draw_l_systems''').fetchall()

        con.close()
        self.tableWidget.setColumnCount(len(head))
        self.tableWidget.setHorizontalHeaderLabels(head)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(table_values):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                try:
                    if j == len(head) - 1:
                        #img = open('res.png', 'wb')
                        #img.write(elem)
                        #img.close()
                        icon = QIcon()
                        icon.addFile('res.jpg')
                        item = QTableWidgetItem()
                        item.setIcon(icon)

                        self.tableWidget.setItem(i, j, item)
                    else:
                        self.tableWidget.setItem(i, j,
                                                 QTableWidgetItem(str(elem)))
                except Exception as e:
                    print(e)
        self.tableWidget.resizeColumnsToContents()
        con.close()

    def filter_table(self, event):
        value = event.data()
        self.update_table(value)