class Player:
    def __init__(self):
        self.warriors = []

    def add_warrior(self, obj):
        self.warriors.append(obj)

    def has_alive_warriors(self):
        for i in self.warriors:
            if i.alive:
                return True
        return False
