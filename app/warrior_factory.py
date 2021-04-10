from app.warrior import Warrior, Archer, Infantryman, Horseman, Swordsman


class Info:
    __list = {}
    obj = None

    def __new__(cls):
        if not cls.obj:
            cls.obj = object.__new__(cls)
        return cls.obj

    @staticmethod
    def getInstance():
        return Info.__list

    @staticmethod
    def addToInstance(name, func):
        if name in Info.__list:
            return
        Info.__list[name] = func


class FactoryRegister:
    def __init__(self, obj):
        self.obj = obj

    def __call__(self, f):
        Info.addToInstance(name=self.obj.__name__, func=f)
        return f


class WarriorFactory:
    def __init__(self):
        a = [cls for cls in WarriorFactory.__subclasses__()]
        for sub_class in a:
            sub_class()

    def create_warrior(self):
        pass


@FactoryRegister(Archer)
class ArcherFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Archer()


@FactoryRegister(Infantryman)
class InfantrymanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Infantryman()


@FactoryRegister(Horseman)
class HorsemanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Horseman()


@FactoryRegister(Swordsman)
class SwordsmanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Swordsman()
