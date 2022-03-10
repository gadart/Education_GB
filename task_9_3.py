class Worker:
    name = None
    surname = None
    position = None
    income = None
    bonus = None

    def __init__(self, name, surname, position, income, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, income, bonus):
        super().__init__(name, surname, position, income, bonus)
    def get_full_name(self):
        return self.name + self.surname
    def get_full_income(self):
        self.__income = {'income': self.income, 'bonus': self.bonus}
        return self.__income

manager = Position('Ivan', 'Ivanov', 'Manager', 10000, 20)
print(manager.get_full_name(), manager.get_full_income())