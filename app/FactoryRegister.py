class Info:
    def __new__(cls):
        if not hasattr(cls, 'obj'):
            cls.obj = object.__new__(cls)
            cls.obj.dict_of_factories = {}
        return cls.obj

    @staticmethod
    def getInstance(cls):
        return Info.__new__(cls).obj

    @staticmethod
    def addToInstance(cls, name, func):
        if name in Info.getInstance(cls).dict_of_factories:
            return
        Info.getInstance(cls).dict_of_factories[name] = func

    @staticmethod
    def get_factories(cls):
        return cls.getInstance(Info).dict_of_factories


class FactoryRegister:
    def __init__(self, obj):
        self.obj = obj

    def __call__(self, f):
        Info.addToInstance(Info, name=self.obj.__name__, func=f)
        return f
