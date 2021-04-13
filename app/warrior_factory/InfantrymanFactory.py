from app.FactoryRegister import FactoryRegister
from app.warrior_factory.WarriorFactory import WarriorFactory
from app.warrior.Infantryman import Infantryman


@FactoryRegister(Infantryman)
class InfantrymanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Infantryman()


InfantrymanFactory()
