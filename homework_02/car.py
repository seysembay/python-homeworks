from homework_02.base import Vehicle
from homework_02.engine import Engine
# from base import Vehicle
# from engine import Engine


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, value):
        self.engine = value

    def __str__(self):
        return f'{self.engine}'


eng = Engine(10, 6)
print(eng)
car_test = Car(20, 100, 3)
car_test.set_engine(eng)
print(car_test)
