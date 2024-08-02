class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название {self.name}, количество этажей {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            print ("Несовпадение типа данных")

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            print ("Несовпадение типа данных")

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            print ("Несовпадение типа данных")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            print ("Несовпадение типа данных")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            print ("Несовпадение типа данных")

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        else:
            print("Несовпадение типа данных")

    def __radd__(self, value):
        self + value

    def __iadd__(self, value):
        self + value

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print ("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print (i+1)

old_building = House("Школа № 61", 3)
new_building = House("VivaNova", 25)
print(str(old_building))
print(str(new_building))
print (new_building < len(old_building))
print (new_building >= len(old_building))
print (new_building != old_building)
old_building + 1
print (f"Теперь школа {len(old_building)}-этажная")