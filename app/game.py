from app.warrior_factory.WarriorFactory import WarriorFactory
from app.FactoryRegister import Info
from app.warrior_factory import ArcherFactory, HorsemanFactory, InfantrymanFactory, SwordsmanFactory


class Game:
    def __init__(self):
        WarriorFactory()
