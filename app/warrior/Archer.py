from app.warrior.Warrior import Warrior


class Archer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 42
        self.power = 12
        self.alive = True
