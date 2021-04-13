from app.FactoryRegister import FactoryRegister
from app.warrior_factory.WarriorFactory import WarriorFactory
from app.warrior.Horseman import Horseman


@FactoryRegister(Horseman)
class HorsemanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Horseman()


HorsemanFactory()
