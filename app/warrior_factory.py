from app.warrior import Warrior, Archer, Infantryman, Horseman, Swordsman


class FactoryRegister:
    list = {}

    def __init__(self, index):
        self.index = index

    def __call__(self, f):
        self.list[self.index] = f
        return f


class WarriorFactory:
    def __init__(self):
        a = [cls for cls in WarriorFactory.__subclasses__()]
        for sub_class in a:
            sub_class()

    def create_warrior(self):
        pass


@FactoryRegister(index=0)
class ArcherFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Archer()


@FactoryRegister(index=1)
class InfantrymanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Infantryman()


@FactoryRegister(index=2)
class HorsemanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Horseman()


@FactoryRegister(index=3)
class SwordsmanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Swordsman()
