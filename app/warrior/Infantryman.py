from app.warrior.Warrior import Warrior


class Infantryman(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 38
        self.power = 17
        self.alive = True
