class Warrior:
    def __init__(self):
        self.power = 0
        self.health = 0
        self.alive = True

    def warrior_status(self, warrior_type):
        return 'type: {}\nhealth: {}\npower: {}\n'.format(warrior_type, self.health, self.power)


class Archer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 42
        self.power = 12
        self.alive = True


class Infantryman(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 38
        self.power = 17
        self.alive = True


class Horseman(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.power = 20
        self.alive = True


class Swordsman(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 36
        self.power = 14
        self.alive = True
