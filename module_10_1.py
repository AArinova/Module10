from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        for i_word in range(1, word_count + 1):
            print(f"Какое-то слово № {i_word}.", file=file)
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}.")

start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

stop = datetime.now()
print('Время выполнения :', stop - start)

start = datetime.now()

t1 = Thread( target=write_words, args=(10, 'example5.txt'))
t1.start()
t1.join()

t2 = Thread( target=write_words, args=(30, 'example6.txt'))
t2.start()
t2.join()

t3 = Thread( target=write_words, args=(200, 'example7.txt'))
t3.start()
t3.join()

t4 = Thread( target=write_words, args=(100, 'example8.txt'))
t4.start()
t4.join()

stop = datetime.now()
print('Время выполнения (потоки) :', stop - start)