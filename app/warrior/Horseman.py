from app.warrior.Warrior import Warrior


class Horseman(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.power = 20
        self.alive = True
