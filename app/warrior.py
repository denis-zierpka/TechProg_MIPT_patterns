from enum import Enum


class WarriorType(Enum):
    Archer = 'Archer'
    Infantryman = 'Infantryman'
    Horseman = 'Horseman'
    Swordsman = 'Swordsman'


class Warrior:
    def __init__(self):
        self.power = 0
        self.health = 0
        self.alive = True

    def attack(self, other):
        other.health -= self.power
        if other.health <= 0:
            other.alive = False


class Archer(Warrior):
    def __init__(self):
        super().__init__()
        self.power = 12
        self.health = 42
        self.type = WarriorType.Archer


class Infantryman(Warrior):
    def __init__(self):
        super().__init__()
        self.power = 17
        self.health = 38
        self.type = WarriorType.Infantryman


class Horseman(Warrior):
    def __init__(self):
        super().__init__()
        self.power = 20
        self.health = 30
        self.type = WarriorType.Horseman


class Swordsman(Warrior):
    def __init__(self):
        super().__init__()
        self.power = 14
        self.health = 36
        self.type = WarriorType.Swordsman
