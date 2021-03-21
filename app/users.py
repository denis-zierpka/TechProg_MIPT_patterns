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

    def perform_attack(self, opp_player, your_warrior, opp_warrior):
        opp_player.warriors[opp_warrior].health -= self.warriors[your_warrior].power
        if opp_player.warriors[opp_warrior].health <= 0:
            opp_player.warriors[opp_warrior].alive = False

    def player_status(self):
        ans = ''
        for i in self.warriors:
            ans += i.warrior_status()
            ans += '\n'
        return ans


player1 = Player()
player2 = Player()
