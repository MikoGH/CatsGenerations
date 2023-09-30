from classClan import *
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
import sys

clan = Clan()
clan.generate_clan(20)

clan.print_clan()
# speed_default = 1
# speed = 0

# class Window(QMainWindow):
#     def __init__(self):
#         super(Window, self).__init__()
        
#         layout = QGridLayout()
#         self.setLayout(layout)

#         # Кнопка. Выход из приложения
#         btn_exit = QtWidgets.QPushButton(self)
#         btn_exit.setFixedSize(200, 40)
#         btn_exit.setText("Exit")
#         btn_exit.clicked.connect(self.close_window)

#         # Кнопка. Генерация клана
#         btn_generate = QtWidgets.QPushButton(self)
#         btn_generate.move(200, 0)
#         btn_generate.setFixedSize(200, 40)
#         btn_generate.setText("Generate")
#         # btn_exit.clicked.connect(self.print_speed)

#         # Кнопка. Скорость - x0
#         btn_speed0 = QtWidgets.QPushButton(self)
#         btn_speed0.move(500, 0)
#         btn_speed0.setFixedSize(40, 40)
#         btn_speed0.setText("|")
#         btn_speed0.clicked.connect(lambda: self.set_speed(0))
        
#         # Кнопка. Скорость - x1
#         btn_speed1 = QtWidgets.QPushButton(self)
#         btn_speed1.move(560, 0)
#         btn_speed1.setFixedSize(40, 40)
#         btn_speed1.setText(">")
#         btn_speed1.clicked.connect(lambda: self.set_speed(1))
        
#         # Кнопка. Скорость - x2
#         btn_speed2 = QtWidgets.QPushButton(self)
#         btn_speed2.move(620, 0)
#         btn_speed2.setFixedSize(40, 40)
#         btn_speed2.setText(">>")
#         btn_speed2.clicked.connect(lambda: self.set_speed(2))
        
#         # Кнопка. Скорость - x3
#         btn_speed3 = QtWidgets.QPushButton(self)
#         btn_speed3.move(680, 0)
#         btn_speed3.setFixedSize(40, 40)
#         btn_speed3.setText(">>>")
#         btn_speed3.clicked.connect(lambda: self.set_speed(3))

#         # Группа. Кнопки скорости
#         gb_speed = QGroupBox("Speed")
#         gb_speed.setCheckable(True)
#         gb_speed.move(700, 0)
#         layout.addWidget(gb_speed)
#         vbox = QVBoxLayout()
#         gb_speed.setLayout(vbox)
#         vbox.addWidget(btn_speed0)
#         vbox.addWidget(btn_speed1)
#         vbox.addWidget(btn_speed2)
#         vbox.addWidget(btn_speed3)

#         self.setWindowTitle("title")

#     ''' Закрытие окна '''
#     def close_window(self):
#         self.close()

#     ''' Измненение скорости '''
#     def set_speed(self, by=0):
#         speed = speed_default * by
#         print(speed)

    


# def application():
#     app = QApplication(sys.argv)
#     app.setStyle('Fusion')
#     window = Window()

#     window.showFullScreen()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     application()