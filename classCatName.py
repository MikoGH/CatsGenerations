import random
import json

''' Имя кота '''
class Cat_Name():
    @property
    def full(self):
        return self.first + self.second
    
    def __init__(self, _first = "", _second = ""):
        self.first = _first  # начало имени
        self.second = _second  # конец имени

    def __str__(self):
        return self.full
    
    def __eq__(self, other):
        return self.full == other
    
    def get_names(name_type="first"):
        with open('names.json') as f:
            data = json.load(f)
            names = dict()  # тег - имена
            for dct in data[name_type]:
                key = list(dct.keys())[0]
                for elm in dct[key]:
                    if elm in names.keys():
                        names[elm].append(key)
                    else:
                        names.update({ elm : [key] })
        return names

    def generate_name_one(name_type, tags):
        names_fit = []
        for tag in tags:
            if name_type == "first":
                if tag in names_first_all.keys():
                    names_fit += names_first_all[tag]
            else:
                if tag in names_second_all.keys():
                    names_fit += names_second_all[tag]
        return random.choice(names_fit).capitalize()
    
    def generate_name(tags):
        name_first = Cat_Name.generate_name_one("first", tags)
        name_second = Cat_Name.generate_name_one("second", tags)
        return Cat_Name(name_first, name_second)
    
names_first_all = Cat_Name.get_names("first")
names_second_all = Cat_Name.get_names("second")