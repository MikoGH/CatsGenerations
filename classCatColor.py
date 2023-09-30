import random
import json

''' Окрас - один цвет '''
class Cat_Color_One():
    def __init__(self, _color, _name):
        self.color = _color
        self.name = _name

    def get_colors(color_type="fur"):
        with open('colors.json') as f:
            data = json.load(f)
            colors = []
            for dct in data[color_type]:
                key = list(dct.keys())[0]
                for elm in dct[key]:
                    colors.append(Cat_Color_One(elm, key))
        return colors

    def generate_color(color_type="fur"):
        if color_type=="fur":
            return random.choice(colors_fur_all)
        else:
            return random.choice(colors_eyes_all)
        
    def combine_color(cat1, cat2, color_type="fur"):
        # 5% шанс мутации цвета
        if random.randint(0,20) == 0:  
            return Cat_Color_One.generate_color(color_type)

        if color_type=="fur":
            return random.choice([cat1.color.primary, cat1.color.secondary, cat2.color.primary, cat2.color.secondary])
        else:
            return random.choice([cat1.color.eyes, cat2.color.eyes])


colors_fur_all = Cat_Color_One.get_colors("fur")  # цвета шерсти с названиями
colors_eyes_all = Cat_Color_One.get_colors("eyes")  # цвета глаз с названиями

''' Окрас - один паттерн '''
# class Cat_Pattern_One():
#     def __init__(self, _name):
#         self.name = _name

#     def __str__(self):
#         return self.name


''' Окрас - все цвета и паттерны '''
class Cat_Color_Full():
    def __init__(self, _color1, _color2, _color3, _patterns):
        self.primary = _color1
        self.secondary = _color2
        self.eyes = _color3
        self.patterns = _patterns

    def generate_color():
        patterns = []
        for i in range(1,10):
            if random.randint(0,3) == 0:
                patterns.append(f"fur{i}")
        return Cat_Color_Full(Cat_Color_One.generate_color("fur"), Cat_Color_One.generate_color("fur"), Cat_Color_One.generate_color("eyes"), patterns)
    
    def combine_color(cat1, cat2):
        # комбинирование паттернов
        patterns = []
        parents_patterns = {f"fur{i}" : 0 for i in range(1,10)}
        for pattern in cat1.color.patterns+cat2.color.patterns:
            parents_patterns[pattern] += 1
        for i in range(1,10):
            # 10% шанс мутации паттерна
            if parents_patterns[f"fur{i}"] == 0 and random.randint(0,10) == 0:
                patterns.append(f"fur{i}")
            # 60% шанс если паттерн у 1 родителя
            if parents_patterns[f"fur{i}"] == 1 and random.randint(0,2) > 0:
                patterns.append(f"fur{i}")
            # 80% шанс если паттерн у 2 родителей
            if parents_patterns[f"fur{i}"] == 2 and random.randint(0,5) > 0:
                patterns.append(f"fur{i}")

        return Cat_Color_Full(Cat_Color_One.combine_color(cat1, cat2, "fur"), Cat_Color_One.combine_color(cat1, cat2, "fur"), Cat_Color_One.combine_color(cat1, cat2, "eyes"), patterns)
    
