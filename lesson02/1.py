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
        self._health: int = health
        self._armor: int = armor
        self.strong: int = strong

    def print_info(self):
        print(f"Перед вами {self.name} со здоровьем {self.health} броней {
              self.armor} и силой атаки {self.strong}!\n")

# формулы от балды
# случайный коэффициент модификации урона
# броня сокращается на 100% от силы удара
# урон зависит от % состояния брони,
# с броней 0.0 урон проходит на 100% :-)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, damage):
        self._health = round((self._health - damage*(100 - self.armor)/100), 2)
        return self._health

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, damage):
        if self._armor > 0:
            self._armor -= damage
        else:
            self._armor = 0.0
        return self._armor

    def kick(self, enemy, luck=1):
        luck = random.randint(1, 10)
        damage = self.strong * luck
        enemy.armor = damage
        enemy.health = damage
        print(f"{self.name} наносит удар {
              damage} своему сопернику {enemy.name}!")
        print(f"В результате у {enemy.name} остается {
              enemy.armor} единиц брони и {enemy.health} единиц здоровья\n")

    def fight(self, enemy):
        while True:
            if self.health > 0:
                self.kick(enemy)
            else:
                print(f"Победил {enemy.name} !")
                break
            if enemy.health > 0:
                enemy.kick(self)
            else:
                print(f"Победил {self.name} !")
                break


fighter1 = Hero(name="James Sullivan", health=100, armor=100, strong=2.0,)
fighter2 = Hero(name="Mike Wazowski", health=100, armor=100, strong=2.0,)

fighter1.print_info()
fighter2.print_info()

fighter1.fight(fighter2)
