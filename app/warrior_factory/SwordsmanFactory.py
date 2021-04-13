from app.FactoryRegister import FactoryRegister
from app.warrior_factory.WarriorFactory import WarriorFactory
from app.warrior.Swordman import Swordsman


@FactoryRegister(Swordsman)
class SwordsmanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Swordsman()


SwordsmanFactory()
