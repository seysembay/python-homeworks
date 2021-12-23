import homework_02.exceptions as exceptions
# import exceptions


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
        max_distance = 0
        if self.fuel > 0 and self.fuel_consumption > 0:
            if self.fuel > self.fuel_consumption:
                max_distance = self.fuel // self.fuel_consumption
        if distance <= max_distance:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel

if __name__ == '__main__':
    car1 = Vehicle(1, 100, 3)
    car1.start()
    car1.move(10)
    print(car1.started)
