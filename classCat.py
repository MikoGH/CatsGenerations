import random
import math
from classCatColor import *
from classCatName import *
from classCatDuty import *
from classCatMoons import *
from classCatImage import *

''' Кот '''
class Cat():
    nextid = 1  # id следующего кота
    def __init__(self, _name, _moons, _lifes, _duty, _color, _gender):
        self.id = Cat.nextid
        Cat.nextid += 1
        self.gender = _gender
        self.name = _name  # полное имя
        self.moons =  _moons  # луны (возраст)
        self.lifes = _lifes  # сколько осталось жизней
        self.alive = True
        self.duty = _duty  # должность
        self.color = _color  # основной и вторичный цвета
        self.image = Cat_Image.set_image(self.color, self.moons.name)

        self.mates = []
        self.parents = []
        self.kits = []
        self.brothers_sisters = []

    def generate_cat():
        color = Cat_Color_Full.generate_color()
        moons = Cat_Moons.generate_moons()
        duty = Cat_Duty.generate_duty(moons)
        name = Cat_Name.generate_name([color.primary.name, color.eyes.name, duty.name])
        gender = random.choice(["male","female"])
        return Cat(name, moons, 9 if duty == "leader" else 1, duty, color, gender)
    
    def generate_kit(cat1, cat2):
        color = Cat_Color_Full.combine_color(cat1, cat2)
        moons = Cat_Moons(0)
        duty = Cat_Duty.generate_duty(moons)
        name = Cat_Name.generate_name([color.primary.name, color.eyes.name, duty.name])
        gender = random.choice(["male","female"])
        return Cat(name, moons, 9 if duty == "leader" else 1, duty, color, gender)
    
    def print_cat(self):
        print(self.name)
        print(self.duty)
        print(self.moons, self.moons.name)
        # print(self.color.primary.name, self.color.primary.color)
        # print(self.color.secondary.name, self.color.secondary.color)
        # print(self.color.eyes.name, self.color.eyes.color)

    


