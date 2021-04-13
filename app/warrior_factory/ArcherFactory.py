from app.FactoryRegister import FactoryRegister
from app.warrior_factory.WarriorFactory import WarriorFactory
from app.warrior.Archer import Archer


@FactoryRegister(Archer)
class ArcherFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Archer()


ArcherFactory()
