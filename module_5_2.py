class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название {self.name}, количество этажей {self.number_of_floors}"

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print ("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print (i+1)

new_building = House("VivaNova", 25)
print(len(new_building))
print(str(new_building))
#new_building.go_to(6)