from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = ''

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)

    def set_engine(self, value):
        self.engine = value


eng = Engine(10, 6)
print(eng)
car_test = Car(20, 100, 3)
car_test.set_engine(eng)
