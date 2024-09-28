from threading import Thread
import time
import random

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        e = 100
        days = 0
        while e > 0:
            e = e - self.power
            time.sleep(1)
            days += 1
            print(f"{self.name} сражается {days} дней, осталось {e} воинов")
        print(f"{self.name} одержал победу спустя {days} дней")
num = random.randint(1, 10)
thr_first = Knight("White Knight", num)
num = random.randint(1, 10)
thr_second = Knight("Black Knight", num)

thr_first.start()
thr_second.start()

thr_first.join()
thr_second.join()

print("Все враги побеждены!")