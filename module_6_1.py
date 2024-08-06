class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if not isinstance(food, Plant):
            return ("Неверный формат данных")
        if food.edible:
            self.fed = True
            return (f"{self.name} съел {food.name}")
        else:
            self.alive = False
            return (f"{self.name} не стал есть {food.name}")

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

tulip = Flower("Мой прекрасный тюльпан")
peach = Fruit("Мой сладкий персик")
elephant = Mammal("Слоненок Дамбо")
dog = Predator("Пес Призрак")
print (elephant.eat(peach))
print(elephant.fed)
print(dog.eat(tulip))
print(dog.alive)
