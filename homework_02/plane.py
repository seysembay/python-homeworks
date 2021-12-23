from homework_02.base import Vehicle
import homework_02.exceptions as exceptions


class Plane(Vehicle):
    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, value):
        if self.cargo + value <= self.max_cargo:
            self.cargo += value
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        tmp = self.cargo
        self.cargo = 0
        return tmp
