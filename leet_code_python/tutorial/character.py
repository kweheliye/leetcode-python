import sys
class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def take_damage(self, amount):
        self.health -= amount


class Warrior(Character):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)
        self.toughness_modifier = 0.90

    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)

warrior = Warrior(100, 50, 10)
print(f"Initial health: {warrior.health}")
warrior.take_damage(40)
print(f"Initial health: {warrior.health}")


 # Abstract tutorial: Run
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bark"

    def move(self):
        return "Run"

dog = Dog()
positive_infinity = float('inf')
print(len(range(sys.maxint)))


try:
    x = 1 / 1
except ZeroDivisionError as e:
    print("Kamal Kamal by zero:", e)
finally:
    print("Cleanup code here")