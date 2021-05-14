import sys

from app.users import Player
from app.warrior_factory import WarriorFactory
from app.warrior.Warrior import Warrior
from app.Facade.facade import Facade
from app.warrior_factory.WarriorFactory import WarriorFactory
from app.FactoryRegister import Info
from app.warrior_factory import ArcherFactory, HorsemanFactory, InfantrymanFactory, SwordsmanFactory


class Game:
    def __init__(self):
        self.facade = Facade()
        WarriorFactory()
        self.player1 = Player()
        self.player2 = Player()

    def add_for_player(self, player, name):
        list_of_items = self.facade.choose_warriors(name)
        for key, val in list_of_items.items():
            print("list_of_items", key, val)
            for _ in range(val):
                player.add_warrior(Info.get_factories(Info)[key].create_warrior(Warrior))

    def attack_player(self, attacker, victim):
        ind_attacker = 0   # from facade
        ind_victim = 0    # from facade

        ind_attacker = int(input())   # TODO
        print(ind_attacker)
        ind_victim = int(input())
        print(ind_victim)

        if not attacker.warriors[ind_attacker].attack(victim.warriors[ind_victim]):
            return False
        return True

    def check_for_win(self):
        if not self.player1.has_alive_warriors():
            print("Player2 won!")
        if not self.player2.has_alive_warriors():
            print("Player1 won!")
        a = int(input())
        sys.exit(0)

    def print_start_info(self):
        print('-----------------')
        print('Player1 status:')
        print(self.player1.player_status())
        print('-----------------')
        print('Player2 status:')
        print(self.player2.player_status())

    def start_battle(self):
        self.add_for_player(self.player1, "Player1")
        self.add_for_player(self.player2, "Player2")

        if len(self.player2.warriors) == 4:
            while True:
                result = self.attack_player(self.player1, self.player2)
                print(666, result)
                while not result:
                    result = self.attack_player(self.player1, self.player2)

                self.print_start_info()
                self.check_for_win()

                result = self.attack_player(self.player2, self.player1)
                while not result:
                    result = self.attack_player(self.player2, self.player1)

                self.print_start_info()
                self.check_for_win()





