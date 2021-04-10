from app.warrior import Warrior, Archer, Infantryman, Horseman, Swordsman


class FactoryRegister:
    list = {}


factory_register = FactoryRegister()


def register(index):
    def wrapper(func):
        factory_register.list[index] = func
        return func
    return wrapper


class WarriorFactory:
    def __init__(self):
        a = [cls for cls in WarriorFactory.__subclasses__()]
        for sub_class in a:
            sub_class()

    def create_warrior(self):
        pass


@register(index=0)
class ArcherFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Archer()


@register(index=1)
class InfantrymanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Infantryman()


@register(index=2)
class HorsemanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Horseman()


@register(index=3)
class SwordsmanFactory(WarriorFactory):
    def __init__(self):
        pass

    def create_warrior(self):
        return Swordsman()
