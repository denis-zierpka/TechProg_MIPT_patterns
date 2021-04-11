class Player:
    def __init__(self):
        self.warriors = []

    def add_warrior(self, obj):
        self.warriors.append(obj)

    def player_status(self):
        ans = ''
        for i in self.warriors:
            ans += i.warrior_status(str(type(i).__name__))
            ans += '\n'
        return ans


player1 = Player()
player2 = Player()
