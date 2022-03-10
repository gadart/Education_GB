class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текушая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость для городской машины {self.name} - {self.speed}')

        if self.speed > 60:
            return f'{self.name} превышение скорости'
        else:
            return f'{self.name} нормальная скорость'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость для рабочей машины {self.name} - {self.speed}')

        if self.speed > 40:
            return f'{self.name} превышение скорости'
        else:
            return f'{self.name} нормальная скорость'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость для рабочей машины {self.name} - {self.speed}')

        if self.speed > 40:
            return f'{self.name} превышение скорости'
        else:
            return f'{self.name} нормальная скорость'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская служебная машина'
        else:
            return f'{self.name} не служебная машина '


audi = SportCar(150, 'Red', 'Audi', False)
kia = TownCar(80, 'White', 'Kia', False)
kamaz = WorkCar(70, 'Yellow', 'KAMAZ', True)
ford = PoliceCar(110, 'Blue', 'Ford', True)
print(kamaz.turn_left())
print(f'{kia.turn_right()}, {audi.stop()}')
print(f'{kamaz.go()} {kamaz.show_speed()}')
print(f'{kamaz.name} is {kamaz.color}')
print(f'{audi.name} полицейская машина? {audi.is_police}')
print(f'{ford.name} полицейская машина? {ford.is_police}')
print(audi.show_speed())
print(kia.show_speed())
print(ford.police())
print(ford.show_speed())
