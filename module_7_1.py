class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f"{self.name}, {self.weight}, {self.category}")

class Shop:
    def __init__(self, __file_name = 'products.txt'):
        self.__file_name = __file_name
        file = open(self.__file_name, 'w')
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        return(f'Товары магазина:\n{file.read()}')
        file.close()

    def add(self, *products):
        result = ""
        for product in products:
            file = open(self.__file_name, 'a')
            if str(product) in self.get_products():
                file.close()
                result += f"Продукт {product} уже есть в магазине\n"
            else:
                file.write(f"{str(product)}\n")
                file.close()
                result += f"Продукт {str(product)} добавлен в магазин\n"
        return (result)

potato = Product("Картофель", "1 кг", "Овощи")
tomato = Product("Помидоры", "1 кг", "Овощи")
apple = Product("Яблоки", "1 кг", "Фрукты")
shop = Shop()
print(shop.add(potato))
print(shop.add(tomato, potato, apple))
print(shop.get_products())