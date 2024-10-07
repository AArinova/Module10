from queue import Queue
from threading import Thread
from random import randint
from time import sleep

class Table:

    def __init__(self, number: int):
        self.number = number
        self.guest = None

class Guest(Thread):

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        """случайное ожидание"""
        wait = randint(3, 10)
        sleep(wait)
class Cafe:

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        """прибытие гостей"""
        for i_guest in guests:
            """гость не усажен за стол"""
            is_sit = False
            for i_table in self.tables:
                if i_table.guest is None:
                    is_sit = True
                    i_table.guest = i_guest
                    i_guest.start()
                    print(f"{i_guest.name} сел(-а) за стол номер {i_table.number}.")
                    break
            if not is_sit:
                self.queue.put(i_guest)
                print(f"{i_guest.name} в очереди.")

    def discuss_guests(self):
        """обслуживание гостей"""
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for i_table in self.tables:
                if i_table.guest is not None and not i_table.guest.is_alive():
                    print(f'{i_table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {i_table.number} свободен')
                    i_table.guest = None
                if i_table.guest is None and not self.queue.empty():
                    guest = self.queue.get()
                    i_table.guest = guest
                    guest.start()
                    print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i_table.number}')

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()