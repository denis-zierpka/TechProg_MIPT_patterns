from app.users import player1, player2
from app.warrior_factory import WarriorFactory
from app.warrior.Warrior import Warrior
from app.draw import GameGraphicsAdapter
from app.warrior_factory.WarriorFactory import WarriorFactory
from app.FactoryRegister import Info
from app.warrior_factory import ArcherFactory, HorsemanFactory, InfantrymanFactory, SwordsmanFactory


def enter_number_mes():
    print('Enter number from 1 to 4, standing for next warriors')
    num = 1
    # qwe = [str(cls.__name__) for cls in Warrior.__subclasses__()]
    # a = {'Archer': 2, '...': 0, '...': 1, '...': 0}
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
                    a = input()
                except Exception:
                    print("Error!")
                    continue

                if a not in Info.getInstance(cls=Info).dict_of_factories:
                    print("Error!")
                    continue
                player.add_warrior(Info.getInstance(cls=Info).dict_of_factories[a].create_warrior(Warrior))
                break

    def start_battle(self):
        it = GameGraphicsAdapter()

        print('Player1:\nChoose 3 warriors you would like to see in your team')
        a = it.choose_warriors("Player1")
        for i, j in a.items():
            for _ in range(j):
                player1.add_warrior(Info.getInstance(cls=Info).dict_of_factories[i].create_warrior(Warrior))

        print('Player2:\nChoose 3 warriors you would like to see in your team')
        a = it.choose_warriors("Player2")
        for i, j in a.items():
            for _ in range(j):
                player2.add_warrior(Info.getInstance(cls=Info).dict_of_factories[i].create_warrior(Warrior))
        print_start_info()
