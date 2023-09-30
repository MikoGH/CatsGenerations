import random
from classCat import *

class Clan():
    @property
    def has_leader(self):  # наличие лидера
        for cat in self.cats:
            if cat.alive and cat.duty == "leader":
                return True
        return False
    @property
    def has_deputy(self):  # наличие помощника
        for cat in self.cats:
            if cat.alive and cat.duty == "deputy":
                return True
        return False
    @property
    def has_medicine(self):  # наличие целителя
        for cat in self.cats:
            if cat.alive and cat.duty == "medicine":
                count += 1
        return count > 0
    @property
    def has_medicine_apprentice(self):  # наличие ученика целителя
        for cat in self.cats:
            if cat.alive and cat.duty == "medicine apprentice":
                return True
        return False
    @property
    def count_cats(self):  # кол-во котов
        return len(self.cats)
    @property
    def count_medicine(self):  # кол-во медкошек
        count = 0
        for cat in self.cats:
            if cat.alive and (cat.duty.name == "medicine" or cat.duty.name == "medicine apprentice"):
                count += 1
        return count
    
    def __init__(self):
        self.name = ""  # название 
        self.cats = []  # коты клана
        
    def generate_clan(self, count_cats):
        for i in range(count_cats):
            self.cats.append(Cat.generate_cat())
        self.set_leader()
        self.set_deputy()
        for i in range(random.randint(1, max(1,len(self.cats)//10))):
            self.set_medicine()
        for i in range(random.randint(min(1,len(self.cats)//10), max(1,len(self.cats)//10))):
            self.set_medicine_apprentice()

    def set_leader(self):
        if not(self.has_leader) and not(self.has_deputy):
            candidates = [cat for cat in self.cats if cat.moons > 35 and cat.duty.name == "warrior" and cat.alive]
            candidate = ""
            if len(candidates)>0:
                candidate = random.choice(candidates)
            else:
                candidate = self.cats[0]
                for cat in self.cats:
                    if cat.moons > candidate.moons and cat.duty.name == "warrior" and cat.alive:
                        candidate = cat
            if candidate != "":
                candidate.duty = Cat_Duty("leader")
                candidate.lifes = 9
                candidate.name.second = Cat_Name.generate_name_one("second", [candidate.duty.name])
        elif not(self.has_leader):
            candidate = ""
            for cat in self.cats:
                if cat.duty.name == "deputy" and cat.alive:
                    candidate = cat
                    break
            if candidate != "":
                candidate.duty = Cat_Duty("leader")
                candidate.lifes = 9
                candidate.name.second = Cat_Name.generate_name_one("second", [candidate.duty.name])

    def set_deputy(self):
        if not(self.has_deputy):
            candidates = [cat for cat in self.cats if cat.moons > 25 and cat.duty.name == "warrior" and cat.alive]
            candidate = ""
            if len(candidates)>0:
                candidate = random.choice(candidates)
            else:
                candidate = self.cats[0]
                for cat in self.cats:
                    if cat.moons > candidate.moons and cat.duty.name == "warrior" and cat.alive:
                        candidate = cat
            if candidate != "":
                candidate.duty = Cat_Duty("deputy")
                # print()
                # candidate.print_cat() #
                # print()

    def set_medicine(self):
        candidates = [cat for cat in self.cats if cat.duty == "warrior"]
        candidate = ""
        if len(candidates)>0:
            candidate = random.choice(candidates)
        if candidate != "" and candidate.duty == "warrior":
            candidate.duty = Cat_Duty("medicine")

    def set_medicine_apprentice(self):
        candidates = [cat for cat in self.cats if cat.duty == "apprentice"]
        candidate = ""
        if len(candidates)>0:
            candidate = random.choice(candidates)
        if candidate != "" and candidate.duty == "apprentice":
            candidate.duty = Cat_Duty("medicine apprentice")

    ''' Изменить кошку по ходу времени '''
    def change_cat(self, cat):
        # если в звездном племени -- не менять
        if not(cat.alive):
            return
        # возраст
        cat.moons += 1
        # изображение
        if cat.moons == 1 or cat.moons == 6 or cat.moons == 16:
            cat.image = Cat_Image.set_image(cat.color, cat.moons.name)
        # должность
        if cat.moons == 6:
            if self.count_medicine <= self.count_cats // 12 or self.count_medicine == 0:
                cat.duty = Cat_Duty("medicine apprentice")
            else:
                cat.duty = Cat_Duty("apprentice")
        if cat.moons == 16:
            if cat.duty.name == "apprentice":
                cat.duty = Cat_Duty("warrior")
            else:
                cat.duty = Cat_Duty("medicine")
        # имя
        if cat.moons == 1 or cat.moons == 6 or cat.moons == 16:
            cat.name.second = Cat_Name.generate_name_one("second", [cat.duty.name])

    ''' Найти партнёров '''
    def set_mates(self):
        candidates_male = [cat for cat in self.cats if cat.alive and cat.moons >= 16 and cat.gender == "male" and cat.duty != "medicine" and (len(cat.mates) == 0 or not(cat.mates[-1].alive))]

        if len(candidates_male) == 0:
            return
        male = random.choice(candidates_male)
        candidates_female = []  # кандидаты по всем условиям
        # bfs обход в глубину
        used = {cat.id : False for cat in self.cats}  # каких кошек уже обошли
        queue = [male]  # очередь кошек
        deep = [0]  # очередь глубин
        used[male.id] = True

        # поиск далёких родственников
        while queue != []:
            candidate = queue[0]
            for cat in candidate.kits + candidate.parents:
                if not(cat.alive):
                    continue
                if used[cat.id]:
                    continue
                if deep[0] > 2 and cat.moons >= 16 and cat.gender == "female" and cat.duty != "medicine" and (len(cat.mates) == 0 or not(cat.mates[-1].alive)) and abs(male.moons - cat.moons) < 16:
                    candidates_female.append(cat)
                queue.append(cat)
                deep.append(deep[0]+1)
                used[cat.id] = True
            queue.pop(0)
            deep.pop(0)

        # поиск не родственников
        for cat in self.cats:
            if used[cat.id] == False and cat.alive and cat.moons >= 16 and cat.gender == "female" and cat.duty != "medicine" and (len(cat.mates) == 0 or not(cat.mates[-1].alive)) and abs(male.moons - cat.moons) < 16:
                candidates_female.append(cat)

        if len(candidates_female) > 0:
            female = random.choice(candidates_female)
            male.mates.append(female)
            female.mates.append(male)

    ''' Сгенерировать потомство '''
    def generate_litter(self):
        candidates_female = [cat for cat in self.cats if cat.gender == "female" and cat.moons.name != "old" and cat.alive and len(cat.mates) > 0 and cat.mates[-1].alive and len(cat.kits) < 4]
        if len(candidates_female) == 0:
            return
        female = random.choice(candidates_female)
        male = female.mates[-1]
        for i in range(random.randint(1,min(4, 4-len(female.kits)))):
            kit = Cat.generate_kit(female, male)
            self.cats.append(kit)
            # братья/сестры
            for bs in list(set(male.kits + female.kits)):
                bs.brothers_sisters.append(kit)
                kit.brothers_sisters.append(bs)
            # родители
            kit.parents.append(female)
            kit.parents.append(male)
            # котята
            female.kits.append(kit)
            male.kits.append(kit)

    ''' Сгенерировать смерти '''
    def generate_die(self, starclan):
        for i in range(1, self.count_cats // 10):
            pos = random.randint(0, self.count_cats-1)
            cat = self.cats[pos]
            if cat.moons.name == "old":
                cat.lifes -= 1
            elif cat.moons.name == "adult" and random.randint(0, 2) == 0:
                cat.lifes -= 1
            elif cat.moons.name == "young" and random.randint(0, 10) == 0:
                cat.lifes -= 1
            elif cat.moons.name == "teen" and random.randint(0, 12) == 0:
                cat.lifes -= 1
            elif cat.moons.name == "kit" and random.randint(0, 16) == 0:
                cat.lifes -= 1

            if cat.lifes == 0:
                cat.alive = False
                starclan.cats.append(cat)
                self.cats.pop(pos)

                # if cat.duty.name == "leader":
                #     self.set_leader()
                # if cat.duty.name == "deputy":
                #     self.set_deputy()
        self.set_leader()
        self.set_deputy()

    ''' Сгенерировать кота '''
    def generate_cat(self):
        cat = Cat.generate_cat()
        self.cats.append(cat)


    ''' Вывести в консоль '''
    def print_clan(self):
        for i in range(len(self.cats)):
            if self.cats[i].alive:
                self.cats[i].print_cat()
                print()

    ''' Отсортировать '''
    def sort_clan(self):
        self.cats = sorted(self.cats, key=lambda x: (not(x.alive), x.duty, -x.moons.moons))


        