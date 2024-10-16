'''
создать класс Hero со след атрибутами:
    свойства:
        - name
        - health
        - armor
        - strong
    
    методы:
        - print_info - вывод информации о герое
        - kick - принимает параметр enemy:Hero и коэффициент силы удара  по дефолту равный 1,
                производит один удар - высчитывает и уменьшает броню и здоровье, 
                выводит информацию в консоль
        - fight - принимает параметр enemy:Hero и производит обмен ударами (поочереди или случайно)
                пока здоровье одного героя не достигнет 0 



                
                
Создать 2 героя, вывести информацию о них, произвести бой между ними, вывести информацию 
о победителе.

'''


import random


class Hero():
    def __init__(self, name: str, health: int, armor: int, strong: int):
        self.name: str = name
        self.health: int = health
        self.armor: int = armor
        self.strong: int = strong

    def print_info(self):
        return dict(self.name, self.health, self.armor, self.strong)

# формулы от балды
# случайный коэффициент модификации урона
# броня сокращается на 100% от силы удара
# урон зависит от силы удара в зависимости от % состояния брони,
# с броней 0.0 урон проходит на 100% от силы удара :-)

    def kick(self, enemy, strong=1.0):
        luck = random.randint(1, 10)
        kick_now = self.strong * luck
        if enemy.armor > 0:
            enemy.armor = round((enemy.armor - kick_now), 2)
        else:
            enemy.armor = 0.0
        enemy.health = round(
            (enemy.health - kick_now*(100 - enemy.armor)/100), 2)
        print(f"Боец {self.name} наносит удар {
              kick_now} своему сопернику {enemy.name}!")
        print(f"В результате у {enemy.name} остается {
              enemy.armor} единиц брони и {enemy.health} единиц здоровья\n")

    def fight(self, enemy):
        while True:
            if self.health > 0:
                self.kick(enemy)
            else:
                print(f"Победил {enemy.name}!")
                break
            if enemy.health > 0:
                enemy.kick(self)
            else:
                print(f"Победил {self.name}!")
                break


fighter1 = Hero(name="James Sullivan", health=100, armor=100, strong=2.0,)
fighter2 = Hero(name="Mike Wazowski", health=100, armor=100, strong=2.0,)

fighter1.fight(fighter2)
