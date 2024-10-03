from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        num_enemy = 100
        num_days = 0
        while( num_enemy > 0):
            sleep(1)
            num_days += 1
            num_enemy -= self.power
            print(f"{self.name} сражается {num_days}>..., осталось {self.power} воинов.")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

threads = []
for i in range(100):
    tread = Knight()
    tread.start()
    threads.append(threads)

for i_thread in threads:
    i_thread.join()
