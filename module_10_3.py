import random
from time import sleep
from threading import Thread, Lock
from time import sleep
from random import randint

class Bank:

    balance = 0
    lock = Lock()

    """Совершает 100 транзакций пополнения средств."""
    def deposit(self):

        for _ in range(100):
            """увеличение баланса на случайное целое число от 50 до 500"""
            addition = random.randint(50, 500)
            self.balance = self.balance + addition
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {addition}. Баланс: {self.balance}.")
            """имитируtnя скорость выполнения пополнения"""
            sleep( 0.001)

    """Совершаает 100 транзакций снятия средств"""
    def take(self):
        for _ in range(100):
            debiting = random.randint(50, 500)
            print(f"\nЗапрос на {debiting}.")
            if debiting <= self.balance:
                """снятие"""
                self.balance = self.balance - debiting
                print(f"Снятие: {debiting}. Баланс: {self.balance}.")
            else:
                print("Запрос отклонён, недостаточно средств.")
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')