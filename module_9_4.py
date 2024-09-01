import random

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for data in data_set:
                file.write(str(data)+'\n')

    return write_everything

class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
my_ball = MysticBall(("голова", "борода", "дорога", "корова", "каравай", "караван", "сарафан", "сорока"))
print(my_ball())
