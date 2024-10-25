class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step = 1):
        self.start = start
        self.stop = stop
        self.pointer = start
        if step == 0:
            raise StepValueError
        else:
            self.step = step

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step < 0 and self.pointer < self.stop) or (self.step > 0 and self.pointer > self.stop):
            print("\nЭлементы перебраны")
            raise StopIteration()
        current_value = self.pointer  # Сохраняем текущее значение
        self.pointer += self.step  # Увеличиваем указатель
        return current_value

while True:
    start = int(input("Введите начальное значение: "))
    stop = int(input("Введите конечное значение: "))
    step = int(input("Введите шаг: "))
    try:
        iterator = Iterator(start, stop, step)
        for i in iterator:
            print(i, end=' ')
    except StepValueError:
        print('Шаг не может быть равен 0')
    quit = input("Для выхода нажмите q: ")
    if quit == 'q':
        break