#Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ

class NameError(Exception):
    def __init__(self, text):
        self.text = text


class NameValidation:

    def __set__(self, instance, name):
        if not name.isalpha() and not name.isspace():
            raise NameError('The name must be of letters')
        instance.__dict__[self.name] = name.capitalize()

    def __set_name__(self, owner, name):
        self.name = name

class Worker:

    name = NameValidation()
    surname = NameValidation()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return f'{sum(self._income.values())}'


a = Position('Pete7', 'Ivan0v', 'plum6er', 30000, 10000)
a.get_full_name()
a.position()
a.get_total_income()

print(f"Информация по сотруднику: {a.get_full_name()} | {a.position} | {a.get_total_income()}")