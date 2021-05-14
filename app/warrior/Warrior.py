class Warrior:
    def __init__(self):
        self.power = 0
        self.health = 0
        self.alive = True

    def attack(self, other_warrior):
        print(other_warrior.alive)
        if not other_warrior.alive:
            return False

        other_warrior.health -= self.power
        if other_warrior.health <= 0:
            other_warrior.health = 0
            other_warrior.alive = False
        return True
