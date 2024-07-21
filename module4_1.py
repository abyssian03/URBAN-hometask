import fake_math as fm
import true_math as tm
import random

random_num = random.randint(1, 100)
print (f"Результат деления {random_num} на 0:")
print("Вариант 1:", fm.divide(random_num, 0))
print("Вариант 2:",tm.divide(random_num, 0))