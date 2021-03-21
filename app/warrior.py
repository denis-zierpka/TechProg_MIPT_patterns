from enum import Enum


class WarriorType(Enum):
    Warrior = 'Warrior'
    Archer = 'Archer'
    Infantryman = 'Infantryman'
    Horseman = 'Horseman'
    Swordsman = 'Swordsman'


class Warrior:
    def __init__(self):
        self.power = 0
        self.health = 0
        self.alive = True
        self.type = WarriorType.Warrior

    def attack(self, other):
        other.health -= self.power
        if other.health <= 0:
            other.alive = False

    def warrior_status(self):
        return 'type: {}\nhealth: {}\npower: {}\n'.format(self.type.value, self.health, self.power)


class Archer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 42
        self.power = 12
        self.alive = True
        self.type = WarriorType.Archer


class Infantryman(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 38
        self.power = 17
        self.alive = True
        self.type = WarriorType.Infantryman


class Horseman(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.power = 20
        self.alive = True
        self.type = WarriorType.Horseman


class Swordsman(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 36
        self.power = 14
        self.alive = True
        self.type = WarriorType.Swordsman


class WarriorList:
    list = [
        Archer,
        Infantryman,
        Horseman,
        Swordsman,
    ]
