#Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ

class InputData:

    def __set__(self, instance, value):
        if type(value) != int and type(value) != float:
            raise TypeError(f'The value of the variable {self.name} is not a number')
        elif value < 0:
            raise ValueError(f'{self.name} - cannot be negative.')
        else:
            instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Road:
    _length = InputData()
    _width = InputData()
    _weight = InputData()
    _depth = InputData()

    def __init__(self, _length, _width, _weight, _depth):

        self._length = _length
        self._width = _width
        self.weight = _weight
        self.depth = _depth

    def massa(self):
        return self._length * self._width * self._weight * self._depth


r1 = Road(20, -5000, 100, 5)
print(f"Weight of the roadway section {r1}")
r1.massa()
