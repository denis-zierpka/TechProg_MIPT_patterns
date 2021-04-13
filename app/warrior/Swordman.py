from app.warrior.Warrior import Warrior


class Swordsman(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 36
        self.power = 14
        self.alive = True
