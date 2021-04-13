class Warrior:
    def __init__(self):
        self.power = 0
        self.health = 0
        self.alive = True

    def warrior_status(self, warrior_type):
        return 'type: {}\nhealth: {}\npower: {}\n'.format(warrior_type, self.health, self.power)