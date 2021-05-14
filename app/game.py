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
        print('{}:\nChoose 3 warriors you would like to see in your team'.format(name))
        list_of_items = self.facade.choose_warriors(name)
        for key, val in list_of_items.items():
            for _ in range(val):
                player.add_warrior(Info.get_factories(Info)[key].create_warrior(Warrior))

    def start_battle(self):
        self.add_for_player(self.player1, "Player1")
        self.add_for_player(self.player2, "Player2")
