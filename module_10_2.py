from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        """Сражение рыцаря"""
        print(f"{self.name}, на нас напали!")
        """Число враго num_enemy"""
        num_enemy = 100
        num_days = 0
        """Пока все враги не сдохнут"""
        while(num_enemy != 0):
            sleep(1)
            num_days += 1
            num_enemy = num_enemy-self.power
            print(f"{self.name} сражается {num_days} дней, осталось {num_enemy} воинов.\n")
        print(f"\n{self.name} одержал победу спустя {num_days} дней(дня)!\n")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

thread1 = first_knight
thread2 = second_knight

thread1.start()
thread2.start()

thread1.join()
thread2.join()
