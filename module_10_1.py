from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        for i_word in range(word_count):
            print(f"Какое-то слово № {i_word}.", file=file)
            #print(f"Какое-то слово № {i_word}.")
            sleep(0.1)
        print(f"Завершилась запись в файл {file_name}.", file=file)

start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example1.txt')
write_words(200, 'example1.txt')
write_words(100, 'example1.txt')
stop = datetime.now()
print('Время выполнения :', stop - start)