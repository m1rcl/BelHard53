'''
создать классы Mage, Knight, Ork унаследовав его от Hero
    новые свойства:
        - special_points - количество спец очков
        - special_points_name - мана, доблесть, ярость
        - special_points_k - коэффициент (множитель ) увеличивающий обычную атаку
    
    новые методы:
        - hello - приветственное сообщение с выводом информации   
        - special_attack - этом удар производится с использованием коэффициента.
                При спец атаке вычитать из спец.очков 1. Невозможен если очков нет.
        - attack - с вероятностью 25% будет использовать спец.способность героя 
                если у него остались спец.очки. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку. 
                Вывести сообщение в консоль о типе и результате атаки.
        
        

добавить класс Arena:
        - атрибут warriors - все воины на арене (тип list)
        - магический метод __init__, который принимает необязательный аргумент warriors.
                Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
                пустым списком.
        - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
                Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
                Если нет, то добавить воина к списку warriors и вывести сообщение на экран
                "{warrior.name} участвует в битве"        
        - метод battle, который не принимает аргументов и симулирует битву. Сперва 
                должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
                исключение ValueError("Количество воинов на арене должно быть больше 1").
                Битва продолжается, пока на арене не останется только один воин. Сперва
                в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
                защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
                из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
                Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
                Вернуть данного воина из метода battle. 
             
             
Создать несколько воинов используя разные классы, добавить их на арену и запустить битву. 
Выжить должен только один.                
'''


import random
import time


class Hero():
    def __init__(self, name: str, health: float, armor: float, strong: float):
        self.name: str = name
        self._health: float = health
        self._armor: float = armor
        self.strong: float = strong

    def print_info(self):
        print(f"Перед вами {self.name} со здоровьем {self.health} броней {
              self.armor} и силой атаки {self.strong}\n")

    @property
    def health(self) -> float:
        return self._health

    @health.setter
    def health(self, damage: float):
        if self._health > 0:
            self._health = round(
                (self._health - damage*(100 - self.armor)/100), 2)
            return self._health
        elif self._health <= 0:
            return self._health

    @property
    def armor(self) -> float:
        return self._armor

    @armor.setter
    def armor(self, damage: float) -> float:
        if self._armor > 0:
            self._armor -= damage
            return self._armor
        elif self._armor < 0:
            self._armor = 0.0
            return self._armor
        else:
            return self._armor

    def kick(self, enemy):
        print(f"{self.name} наносит обычный удар на величину {
              self.strong} своему сопернику {enemy.name}")
        enemy.armor = self.strong
        enemy.health = self.strong
        print(f"В результате у {enemy.name} остается {
              enemy.armor} единиц брони и {enemy.health} единиц здоровья\n")

    def fight(self, enemy):
        while True:
            if self.health > 0:
                self.kick(enemy)
            else:
                print(f"Победил {enemy.name} !")
                break
            # time.sleep(2)
            if enemy.health > 0:
                enemy.kick(self)
            else:
                print(f"Победил {self.name} !")
                break


class Mage(Hero):
    def __init__(self, name: str, health: float, armor: float, strong: float, special_points: int, special_points_name: str, special_points_k: float):
        super().__init__(name, health, armor, strong)
        self._special_points: int = special_points
        self.special_points_name: str = special_points_name
        self.special_points_k: float = special_points_k

    @property
    def special_points(self) -> int:
        return self._special_points

    @special_points.setter
    def special_points(self, value: int) -> int:
        self._special_points -= value
        return self._special_points

    def hello(self):
        print(f"В битве участвует {self.name} со здоровьем {self.health} броней {self.armor}, силой атаки {self.strong}, имеет {
              self.special_points_name} в количестве {self.special_points} и коэффициентом атаки {self.special_points_k}\n")

    def special_attack(self, enemy):
        self.special_points = 1
        print(f"{self.name} используя {self.special_points_name} наносит спец.удар на величину {
              self.strong*self.special_points_k} своему сопернику {enemy.name}. Осталось {self.special_points} спец.очков")
        enemy.armor = self.strong*self.special_points_k
        enemy.health = self.strong*self.special_points_k
        print(f"В результате у {enemy.name} остается {
              enemy.armor} единиц брони и {enemy.health} единиц здоровья\n")

    def attack(self, enemy):
        make_attack = random.randint(1, 4)
        if self.special_points > 1 and make_attack == 4:
            self.special_attack(enemy)
        else:
            self.kick(enemy)


class Knight(Hero):
    def __init__(self, name: str, health: float, armor: float, strong: float, special_points: int, special_points_name: str, special_points_k: float):
        super().__init__(name, health, armor, strong)
        self._special_points: int = special_points
        self.special_points_name: str = special_points_name
        self.special_points_k: float = special_points_k

    @property
    def special_points(self) -> int:
        return self._special_points

    @special_points.setter
    def special_points(self, value: int) -> int:
        self._special_points -= value
        return self._special_points

    def hello(self):
        print(f"В битве участвует {self.name} со здоровьем {self.health} броней {self.armor}, силой атаки {self.strong}, имеет {
              self.special_points_name} в количестве {self.special_points} и коэффициентом атаки {self.special_points_k}\n")

    def special_attack(self, enemy):
        self.special_points = 1
        print(f"{self.name} используя {self.special_points_name} наносит спец.удар на величину {
              self.strong*self.special_points_k} своему сопернику {enemy.name}. Осталось {self.special_points} спец.очков")
        enemy.armor = self.strong*self.special_points_k
        enemy.health = self.strong*self.special_points_k
        print(f"В результате у {enemy.name} остается {
              enemy.armor} единиц брони и {enemy.health} единиц здоровья\n")

    def attack(self, enemy):
        make_attack = random.randint(1, 4)
        if self.special_points > 1 and make_attack == 4:
            self.special_attack(enemy)
        else:
            self.kick(enemy)


class Ork(Hero):
    def __init__(self, name: str, health: float, armor: float, strong: float, special_points: int, special_points_name: str, special_points_k: float):
        super().__init__(name, health, armor, strong)
        self._special_points: int = special_points
        self.special_points_name: str = special_points_name
        self.special_points_k: float = special_points_k

    @property
    def special_points(self) -> int:
        return self._special_points

    @special_points.setter
    def special_points(self, value: int) -> int:
        self._special_points -= value
        return self._special_points

    def hello(self):
        print(f"В битве участвует {self.name} со здоровьем {self.health} броней {self.armor}, силой атаки {self.strong}, имеет {
              self.special_points_name} в количестве {self.special_points} и коэффициентом атаки {self.special_points_k}\n")

    def special_attack(self, enemy):
        self.special_points = 1
        print(f"{self.name} используя {self.special_points_name} наносит спец.удар на величину {
              self.strong*self.special_points_k} своему сопернику {enemy.name}. Осталось {self.special_points} спец.очков")
        enemy.armor = self.strong*self.special_points_k
        enemy.health = self.strong*self.special_points_k
        print(f"В результате у {enemy.name} остается {
              enemy.armor} единиц брони и {enemy.health} единиц здоровья\n")

    def attack(self, enemy):
        make_attack = random.randint(1, 4)
        if self.special_points > 1 and make_attack == 4:
            self.special_attack(enemy)
        else:
            self.kick(enemy)


class Arena():
    def __init__(self, warriors: list = []):
        self.warriors: list = warriors

    def add_warrior(self, warrior):
        if warrior.name not in [awailable_warrior.name for awailable_warrior in self.warriors]:
            self.warriors.append(warrior)
            warrior.hello()
        else:
            raise ValueError("Воин уже на арене")

    def battle(self):
        if len(self.warriors) < 2:
            raise ValueError("Количество воинов на арене должно быть больше 1")
        while len(self.warriors) > 1:
            current_fighter = random.choice(self.warriors)
            current_enemy = random.choice(self.warriors)
            while current_enemy == current_fighter:
                current_enemy = random.choice(self.warriors)
            current_fighter.attack(current_enemy)
            if current_enemy.health <= 0:
                print(f"{current_enemy.name} пал в битве\n")
                current_arena.warriors.remove(current_enemy)

        print(f"Победил {self.warriors[0].name} !")


current_arena: Arena = Arena()

fighter1 = Mage(name="Mage1", health=80, armor=50, strong=5.0,
                special_points=10, special_points_name='Мана', special_points_k=10)
fighter2 = Knight(name="Knight1", health=100, armor=100, strong=10.0,
                  special_points=10, special_points_name='Доблесть', special_points_k=3)
fighter3 = Ork(name="Ork1", health=120, armor=75, strong=15.0,
               special_points=10, special_points_name='Ярость', special_points_k=2)
fighter4 = Ork(name="Ork1", health=120, armor=75, strong=15.0,
               special_points=10, special_points_name='Ярость', special_points_k=2)

current_arena.add_warrior(fighter1)
current_arena.add_warrior(fighter2)
current_arena.add_warrior(fighter3)
current_arena.add_warrior(fighter4)

current_arena.battle()
