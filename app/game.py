from app.users import Player
from app.warrior_factory import WarriorFactory
from app.warrior.Warrior import Warrior
from app.Facade.facade import Facade
from app.warrior_factory.WarriorFactory import WarriorFactory
from app.FactoryRegister import Info
from app.warrior_factory import ArcherFactory, HorsemanFactory, InfantrymanFactory, SwordsmanFactory


def enter_number_mes():
    print('Enter number from 1 to 4, standing for next warriors')
    num = 1
    for cls in Warrior.__subclasses__():
        print(str(num) + ' ' + str(cls.__name__))
        num += 1
    print('-----------------')





class Game:
    def __init__(self):
        self.facade = Facade()
        WarriorFactory()
        self.player1 = Player()
        self.player2 = Player()

    def choose_warriors(self, player):
        enter_number_mes()
        for i in range(3):
            while True:
                try:
                    a = input()
                except Exception:
                    print("Error!")
                    continue

                if a not in Info.get_factories(Info):
                    print("Error!")
                    continue
                player.add_warrior(Info.get_factories(Info)[a].create_warrior(Warrior))
                break

    def print_start_info(self):
        print('-----------------')
        print('Player1 status:')
        print(self.player1.player_status())
        print('-----------------')
        print('Player2 status:')
        print(self.player2.player_status())

    def add_for_player(self, player, name):
        print('{}:\nChoose 3 warriors you would like to see in your team'.format(name))
        list_of_items = self.facade.choose_warriors(name)
        for key, val in list_of_items.items():
            for _ in range(val):
                player.add_warrior(Info.get_factories(Info)[key].create_warrior(Warrior))

    def start_battle(self):
        self.add_for_player(self.player1, "Player1")
        self.add_for_player(self.player2, "Player2")

        self.print_start_info()
