import random

class Hero:
    """The hero blueprint will be implemented later in the project."""

    def _init_(self,name):
        self.name = name
        self.health = 150
        self.attack_power = 15

    def attack(self):
        random.randint(0, self.attack_power)

    def take_damage(self,damage):
        self.health = max(0,self.health - damage) 

    def is_alive(self):
        return self.health > 0


