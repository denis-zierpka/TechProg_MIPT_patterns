from app.graphics.draw import GameGraphics


class Facade:
    __this = None

    def __new__(cls, *args, **kwargs):
        if cls.__this is None:
            cls.__this = object.__new__(cls)
            return cls.__this

    def __init__(self):
        self.object = GameGraphics()

    def choose_warriors(self, player):
        return self.object.choose_warriors(player)