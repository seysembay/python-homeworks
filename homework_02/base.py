import exceptions


class Vehicle:
    started = False

    def __init__(self, weight=100, fuel=10, fuel_consumption=30):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise exceptions.LowFuelError

    def move(self, distance):
        pass


if __name__ == '__main__':
    car1 = Vehicle(1, 0, 30)
    print(car1.started)
    car1.start()
    print(car1.started)
