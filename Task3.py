#Создать метакласс для паттерна Синглтон


class MetaSingleton(type):
    _instances = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
        return self._instances[self]


class Singleton(metaclass=MetaSingleton):
    pass

sing1 = Singleton()
sing2 = Singleton()
print(sing1 == sing2)