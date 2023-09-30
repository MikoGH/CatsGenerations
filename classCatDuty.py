import random

''' Должность '''
class Cat_Duty():
    def __init__(self, _duty):
        self.name = _duty
        self.value = ["leader","deputy","medicine","warrior","medicine apprentice","apprentice","kit"].index(self.name)
        
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value

    def generate_duty(moons):
        if moons < 6:
            new_duty = "kit"
        elif moons < 16:
            new_duty = "apprentice"
        else:
            new_duty = "warrior"
        return Cat_Duty(new_duty)
    