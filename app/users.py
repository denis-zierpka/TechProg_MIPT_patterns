class Player:
    def __init__(self):
        self.warriors = []

    def add_warrior(self, obj):
        self.warriors.append(obj)

    def has_alive_warrior(self):
        for i in self.warriors:
            if i.alive:
                return True
        return False

    def status(self):
        ans = ''
        for i in self.warriors:
            ans += str(i.type.value) + ' '
        return ans


player1 = Player()
player2 = Player()
