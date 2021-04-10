from app.users import player1, player2
from app.warrior_factory import factory_register
from app.warrior_factory import WarriorFactory
from app.warrior import Warrior


def enter_number_mes():
    print('Enter number from 1 to 4, standing for next warriors')
    num = 1
    for cls in Warrior.__subclasses__():
        print(str(num) + ' ' + str(cls.__name__))
        num += 1
    print('-----------------')


def print_start_info():
    print('-----------------')
    print('Player1 status:')
    print(player1.player_status())
    print('-----------------')
    print('Player2 status:')
    print(player2.player_status())


class Game:
    def __init__(self):
        self.winner = 0
        WarriorFactory()

    def choose_warriors(self, player):
        enter_number_mes()
        for i in range(3):
            while True:
                try:
                    a = int(input())
                except Exception:
                    print("Error!")
                    continue

                if a < 1 or a > 4:
                    print("Error!")
                    continue
                player.add_warrior(factory_register.list[a - 1].create_warrior(Warrior))
                break

    def start_battle(self):
        print('Player1:\nChoose 3 warriors you would like to see in your team')
        self.choose_warriors(player1)
        print('Player2:\nChoose 3 warriors you would like to see in your team')
        self.choose_warriors(player2)

        print_start_info()

    def play(self):
        # implement graphics
        self.start_battle()
