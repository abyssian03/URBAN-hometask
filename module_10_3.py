import threading
import random
import time

class Bank:
    def __init__(self, balance, lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            num = random.randint(50, 500)
            self.balance += num
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение {num}, баланс {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            num = random.randint(50, 500)
            print("Запрос на", num)
            if self.balance >= num:
                self.balance -= num
                print(f"Снятие {num}, баланс {self.balance}")
                time.sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

lock = threading.Lock()
bank = Bank(1, lock)
thread1 = threading.Thread(target=bank.deposit)
thread2 = threading.Thread(target=bank.take)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Итоговый баланс:", bank.balance)
