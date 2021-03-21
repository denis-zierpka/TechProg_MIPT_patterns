from enum import Enum


class WarriorType(Enum):
    Warrior = 'Warrior'
    Archer = 'Archer'
    Infantryman = 'Infantryman'
    Horseman = 'Horseman'
    Swordsman = 'Swordsman'


class Warrior:
    type = WarriorType.Warrior

    def __init__(self):
        self.power = 0
        self.health = 0
        self.alive = True

    def attack(self, other):
        other.health -= self.power
        if other.health <= 0:
            other.alive = False

    def warrior_status(self):
        return 'type: {}\nhealth: {}\npower: {}\n'.format(self.type.value, self.health, self.power)


class Archer(Warrior):
    type = WarriorType.Archer

    def __init__(self):
        super().__init__()
        self.health = 42
        self.power = 12
        self.alive = True


class Infantryman(Warrior):
    type = WarriorType.Infantryman

    def __init__(self):
        super().__init__()
        self.health = 38
        self.power = 17
        self.alive = True


class Horseman(Warrior):
    type = WarriorType.Horseman

    def __init__(self):
        super().__init__()
        self.health = 30
        self.power = 20
        self.alive = True


class Swordsman(Warrior):
    type = WarriorType.Swordsman

    def __init__(self):
        super().__init__()
        self.health = 36
        self.power = 14
        self.alive = True


class WarriorList:
    list = [
        Archer,
        Infantryman,
        Horseman,
        Swordsman,
    ]
