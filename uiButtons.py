from ui import *
from uiCard import *
from classClan import *
from PyQt5.QtGui import QPixmap,QPicture,QMouseEvent
from PIL.ImageQt import ImageQt

selected_color = "blue"
brother_sister_color = "blue"
parent_color = "magenta"
mate_color = "red"
kit_color = "pink"

''' Класс обработчик событий '''
class Ui_MainWindowActions(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.speed_default = 3000  # 1 second
        self.speed = 0
        self.year = 1
        self.moon = 1
        self.clan = Clan()
        self.starclan = Clan()

        self.selected_cat = None

        self.MainWindow = MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        # кнопки скорости
        self.buttons_speed = [self.ui.btn_speed0, self.ui.btn_speed1, self.ui.btn_speed2, self.ui.btn_speed3]

        # таймер
        self.ui.checkThreadTimer = QtCore.QTimer(MainWindow)
        self.set_speed(0)

        # подключение функций
        self.set_functions()

    ''' Привязать элементам функции '''
    def set_functions(self):
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_generate.clicked.connect(self.generate_clan)
        self.ui.btn_speed0.clicked.connect(lambda: self.set_speed(0))
        self.ui.btn_speed1.clicked.connect(lambda: self.set_speed(1))
        self.ui.btn_speed2.clicked.connect(lambda: self.set_speed(2))
        self.ui.btn_speed3.clicked.connect(lambda: self.set_speed(3))
        self.ui.btn_speed_manual.clicked.connect(lambda: self.set_speed(0))
        self.ui.btn_speed_manual.clicked.connect(lambda: self.set_time(True))
        self.ui.btn_speed_manual.clicked.connect(self.set_clan)
        self.ui.checkThreadTimer.timeout.connect(self.set_time)
        self.ui.checkThreadTimer.timeout.connect(self.set_clan)

    ''' Закрыть приложение '''
    def close(self):
        self.MainWindow.close()

    ''' Изменить скорость '''
    def set_speed(self, by):
        for i in range(len(self.buttons_speed)):
            self.buttons_speed[i].setAutoFillBackground(False)
        self.buttons_speed[by].setAutoFillBackground(True)
        if by == 0:
            self.ui.checkThreadTimer.stop()
        else:
            self.speed = self.speed_default * 1/by
            self.ui.checkThreadTimer.start()
            self.ui.checkThreadTimer.setInterval(self.speed) 

    ''' Задать цвет кнопки '''
    def fill_btn_pellette(self, btn, color):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(color)
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)        
        btn.setPalette(palette)

    ''' Установить соответствующие год и месяц '''
    def set_time(self, show=True):
        if self.moon == 12:
            self.year += 1
            self.moon = 1
        else:
            self.moon += 1

        # изменить котов по ходу времени
        for i in range(len(self.clan.cats)):
            self.clan.change_cat(self.clan.cats[i])
        self.clan.set_mates()
        # 10% шанс потомства раз в луну
        if random.randint(0, 10) == 0:
            self.clan.generate_litter()
        # 50% шанс смертей раз в луну
        if random.randint(0, 1) == 0:
            self.clan.generate_die(self.starclan)
        # 10% шанс нового кота вне клана раз в луну
        # 100% шанс нового кота если <10 котов 
        if random.randint(0, 10) == 0 or self.clan.count_cats < 16:
            self.clan.generate_cat()

        self.clan.sort_clan()

        if show:
            self.ui.lbl_season.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:{['#5056ab', '#c0468b', '#50c66b', '#f0962b'][(self.moon)%12 // 3]};\">{['leaf-bare', 'newleaf', 'greenleaf', 'fall-leaf'][(self.moon)%12 // 3]}</span></p></body></html>")
            self.ui.lbl_years_count.setText(f"<html><head/><body><p align=\"center\">{self.year}</p></body></html>")
            self.ui.lbl_moons_count.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#10116b;\">{self.moon}</span></p></body></html>")
            self.set_clan()

    ''' Установить данные клана '''
    def set_clan(self):
        self.ui.lbl_cats_count.setText(f"<html><head/><body><p align=\"center\">{self.clan.count_cats}</p></body></html>")

        # карточки
        self.columns = 3
        for i in reversed(range(self.ui.layout_cats.count())):
            widget_to_remove = self.ui.layout_cats.itemAt(i)
            if widget_to_remove != None and widget_to_remove.widget() != None:
                widget_to_remove.widget().setParent(None)
                self.ui.layout_cats.removeWidget(widget_to_remove.widget())

        for i in range(self.clan.count_cats):
            widget_card = QtWidgets.QWidget()
            self.set_card(widget_card, self.clan.cats[i])
            self.ui.layout_cats.addWidget(widget_card, i//self.columns, i%self.columns, QtCore.Qt.AlignTop)
            
        verticalSpacer = QtWidgets.QSpacerItem(40, 20,  QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui.layout_cats.addItem(verticalSpacer, 6, 0, QtCore.Qt.AlignTop)
        self.ui.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(self.columns * widget_card.width() + 30, (self.clan.count_cats+self.columns-1)//self.columns * (widget_card.height()+1)))
        self.ui.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(self.columns * widget_card.width() + 30, (self.clan.count_cats+self.columns-1)//self.columns * (widget_card.height()+1)))
        

    ''' Выделить кошку '''
    def select_cat(self, cat):
        if self.selected_cat == cat:
            self.selected_cat = None
        else:
            self.selected_cat = cat


    ''' Установить цвет карточки '''
    def set_card_color(self, ui_widget, cat):
        border = 0
        color = "white"
        text = ""
        if self.selected_cat != None:
            if cat == self.selected_cat:
                border = 6
                color = selected_color
            elif len(self.selected_cat.mates) > 0 and cat == self.selected_cat.mates[-1]:
                border = 2
                color = mate_color
                text = "*mate"
            elif cat in self.selected_cat.brothers_sisters:
                border = 2
                color = brother_sister_color
                if cat.gender == "female":
                    text = "*sister"
                else:
                    text = "*brother"
            elif cat in self.selected_cat.parents:
                border = 2
                color = parent_color
                if cat.gender == "female":
                    text = "*mother"
                else:
                    text = "*father"
            elif cat in self.selected_cat.kits:
                border = 2
                color = kit_color
                text = "*kit"
        ui_widget.lbl_relationship.setText(f"<body><html><span style=\" color:{color};\">{text}</span></body></html>")
        ui_widget.btn_highlight.setStyleSheet(f"border: {border}px solid {color};")


    ''' Установить данные карточки '''
    def set_card(self, widget_card, cat):
        ui_widget = Ui_widget_card()
        ui_widget.setupUi(widget_card)
        self.set_card_color(ui_widget, cat)
        # ui_widget.lbl_id.setHidden(True)
        ui_widget.btn_highlight.clicked.connect(lambda: self.select_cat(cat))
        ui_widget.btn_highlight.clicked.connect(self.set_clan)
        ui_widget.lbl_name.setText(cat.name.full)
        
        dct = {'leader':'#ff5522', 'deputy':'#ee9922', 'medicine':'#222299', 'warrior':'#229922', 'medicine apprentice':'#227799', 'apprentice':'#227777', 'kit':'#444455'}
        ui_widget.lbl_duty.setText(f"<html><head/><body><span style=\" color:{dct[cat.duty.name]};\">{cat.duty.name}</span></body></html>")
            
        ui_widget.lbl_gender.setText("♂" if cat.gender == "male" else "♀")
        ui_widget.lbl_moons.setText("%3d | %d"%(cat.moons.moons, cat.lifes))
        ui_widget.lbl_moons_name.setText(cat.moons.name)
        ui_widget.lbl_image.setPixmap(QPixmap.fromImage(ImageQt(cat.image)))
        color_starclan = '#888888'
        color_alive = '#000000'

        # mate
        # if self.selected_cat == cat:
        #     color_alive = mate_color
        ui_widget.lbl_mate.setText(f"<body><html>mates: ")
        for mate in cat.mates:
            ui_widget.lbl_mate.setText(ui_widget.lbl_mate.text()+f"<span style=\" color:{[color_starclan,color_alive][mate.alive]};\">{'♂' if mate.gender == 'male' else '♀'}{mate.name} </span>")
        ui_widget.lbl_mate.setText(ui_widget.lbl_mate.text()+f"</body></html>")
        # kits
        # if self.selected_cat == cat:
        #     color_alive = kit_color
        ui_widget.lbl_kits.setText(f"<body><html>kits: ")
        for kit in cat.kits:
            ui_widget.lbl_kits.setText(ui_widget.lbl_kits.text()+f"<span style=\" color:{[color_starclan,color_alive][kit.alive]};\">{'♂' if kit.gender == 'male' else '♀'}{kit.name} </span>")
        ui_widget.lbl_kits.setText(ui_widget.lbl_kits.text()+f"</body></html>")
        # parents
        # if self.selected_cat == cat:
        #     color_alive = parent_color
        ui_widget.lbl_parents.setText(f"<body><html>parents: ")
        for parent in cat.parents:
            ui_widget.lbl_parents.setText(ui_widget.lbl_parents.text()+f"<span style=\" color:{[color_starclan,color_alive][parent.alive]};\">{'♂' if parent.gender == 'male' else '♀'}{parent.name} </span>")
        ui_widget.lbl_parents.setText(ui_widget.lbl_parents.text()+f"</body></html>")
        # brothers/sisters
        # if self.selected_cat == cat:
        #     color_alive = brother_sister_color
        ui_widget.lbl_brothers_sisters.setText(f"<body><html>brothers/sisters: ")
        # ui_widget.lbl_brothers_sisters.setText(f"<html><body>brothers/sisters: ")
        for bs in cat.brothers_sisters:
            ui_widget.lbl_brothers_sisters.setText(ui_widget.lbl_brothers_sisters.text()+f"<span style=\" color:{[color_starclan,color_alive][bs.alive]};\">{'♂' if bs.gender == 'male' else '♀'}{bs.name} </span>")
        ui_widget.lbl_brothers_sisters.setText(ui_widget.lbl_brothers_sisters.text()+f"</body></html>")

    ''' Сгенерировать новый клан '''
    def generate_clan(self):
        self.set_speed(0)
        self.clan = Clan()
        self.clan.generate_clan(30)
        # спустя 100 лун
        for i in range(100):
            self.set_time(False)
        self.year = -1
        self.moon = 12
        self.set_time(True)


