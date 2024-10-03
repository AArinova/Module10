from threading import Thread

class Knight(Thread):

    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)