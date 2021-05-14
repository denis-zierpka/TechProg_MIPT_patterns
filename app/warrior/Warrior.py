class Warrior:
    def __init__(self):
        self.power = 0
        self.health = 0
        self.alive = True

    def attack(self, other_warrior):
        if not other_warrior.alive:
            return False
        if not self.alive:
            return False

        other_warrior.health -= self.power
        if other_warrior.health <= 0:
            other_warrior.health = 0
            other_warrior.alive = False
        return True

    def warrior_status(self, warrior_type):
        return 'type: {}\nhealth: {}\npower: {}\n'.format(warrior_type, self.health, self.power)
