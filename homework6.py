my_dict = {"Анна": 1983, "Андрей": 1982, "Леонид": 1985}
print(my_dict)
print("Анна:", my_dict.get("Анна"))
print(my_dict.get("Яна", "такого ключа нет"))
my_dict.update({"Виталий": 1989, "Кирилл": 1978})
print("Андрей:", my_dict.pop("Андрей"))
print(my_dict)
#другой вариант:
#print(my_dict.items())
my_set = {19, 8, 5, "красный", 5, "синий", 11, 8}
print(my_set)
my_set.update({True, False})
my_set.discard(19)
print(my_set)