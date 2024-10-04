import random
import time
from threading import Thread
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, tables, queue):
        self.tables = tables
        self.queue = queue

    def guest_arrival(self, *guests):
        try:
            for guest in guests:
                flag = False
                for table in self.tables:
                    if table.guest == None:
                        table.guest = guest
                        print (f"{guest.name} сел(а) за стол {table.number}")
                        table.guest.start()
                        flag = True
                        break
                if flag == True:
                    continue
                self.queue.put(guest)
                print(f"{guest.name} в очереди")
        except:
            print ("Некорректные данные")
            name = input("Введите имя гостя: ")
            guest_arrival(name)

    def discuss_guests(self):
        while True:
            if all([table.guest == None for table in self.tables]) and self.queue.empty():
                return ("Обслуживание закончено")
            else:
                for table in self.tables:
                    if table.guest == None:
                        if not self.queue.empty():
                            table.guest = queue.get()
                            print(f"Гость {table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                            table.guest.start()
                        else:
                            continue
                    elif table.guest.is_alive():
                         print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                         print(f"Стол номер {table.number} свободен")
                         table.guest = None

queue = Queue()
ivanov = Guest('Ivanov')
petrov = Guest('Petrov')
sidorov = Guest('Sidorov')
my_cafe = Cafe((Table(1), Table(2)), queue)
my_cafe.guest_arrival(ivanov, petrov, sidorov)
print(my_cafe.discuss_guests())
