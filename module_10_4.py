import queue
from threading import Thread
from random import randint
from time import sleep


class Table:

    def __init__(self, number: int, guest = None):
        self.number = number
        self.guest = guest

    """усаживаем гостя за стол"""
    def sit_guest(self, guest_name: str):
        if self.guest != None:
            return False
        else:
            self.guest = guest_name
            return True

class Guest(Thread):

    def __idiv__(self, name: str):
        self.name = name

    def run(self):
        """случайное ожидание"""
        wait = randint(3, 10)
        print('Задержка', wait)
        sleep(wait)

class Cafe:

    def __init__(self, queue: queue, tables: list):
        self.queue = queue
        self.tables = tables

    def guest_arrival(self, guests: list):
        """прибытие гостей"""
        for i_guest in guests:
            is_sit = False
            for i_table in self.tables:
                if i_table.sit_quest(i_guest.name) == True:
                    is_sit = True
                    print(f"{i_guest.name} сел(-а) за стол номер {i_table.number}.")
                    break
            if is_sit == False:
                self.queue.put(i_guest)
                print(f"{i_guest.name} в очереди.")


    def discuss_guests(self):
        """обслужитвание гостей"""
        pass

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
#cafe.discuss_guests()