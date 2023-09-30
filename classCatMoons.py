import random
import math

''' Возраст кота '''
class Cat_Moons():
    def __init__(self, _moons):
        self.moons = _moons 
        self.name = Cat_Moons.set_name(_moons)

    def __str__(self):
        return str(self.moons)

    def set_name(_moons):
        if _moons < 6:
            return "kit"
        if _moons < 16:
            return "teen"
        if _moons < 32:
            return "young"
        if _moons < 90:
            return "adult"
        else:
            return "old"
        
    def __eq__(self, other):
        if type(other) == Cat_Moons:
            return self.moons == other.moons
        else:
            return self.moons == other
    
    def __lt__(self, other):
        if type(other) == Cat_Moons:
            return self.moons < other.moons
        else:
            return self.moons < other
    
    def __le__(self, other):
        if type(other) == Cat_Moons:
            return self.moons <= other.moons
        else:
            return self.moons <= other
    
    def __gt__(self, other):
        if type(other) == Cat_Moons:
            return self.moons > other.moons
        else:
            return self.moons > other
    
    def __ge__(self, other):
        if type(other) == Cat_Moons:
            return self.moons >= other.moons
        else:
            return self.moons >= other
        
    def __iadd__(self, other):
        if type(other) == Cat_Moons:
            self.moons += other.moons
        else:
            self.moons += other
        self.name = Cat_Moons.set_name(self.moons)
        return self
    
    def __add__(self, other):
        if type(other) == Cat_Moons:
            return self.moons + other.moons
        else:
            return self.moons + other
        
    def __sub__(self, other):
        if type(other) == Cat_Moons:
            return self.moons - other.moons
        else:
            return self.moons - other

    def generate_moons():
        m = 5000
        x = random.randint(0, m)
        return Cat_Moons(round(math.sqrt(m) - math.sqrt(x)))
    
    
