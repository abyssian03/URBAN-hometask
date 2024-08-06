class Vehicle:
    __COLOR_VARIANTS = ["черный", "белый", "красный", "зеленый", "желтый", "синий" ]

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return (f"Модель: {self.__model}")

    def get_horsepower(self):
        return (f"Мощность двигателя: {self.__engine_power} л. с.")

    def get_color(self):
        return (f"Цвет: {self.__color}")

    def print_info(self):
        print(f"ИНФО\n{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}"
              f"\nВладелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self._Vehicle__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

my_virtual_car = Sedan("Анна Моисеева", "Ford Fiesta", 200, "красный")
my_virtual_car.set_color("сиреневый")
my_virtual_car.set_color("ЧЕРНЫЙ")
my_virtual_car.print_info()
