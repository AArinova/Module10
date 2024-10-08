from multiprocessing import Pool
from datetime import datetime

def read_info(name):

    with open(name, "r", encoding='utf-8') as file:
        while True:
            line = file.readline()
            print(line)

if __name__ == '__main__':

    start = datetime.now()
    read_info('file 1.txt')
    stop = datetime.now()
    print('Время выполнения:', stop - start)
    #
    # print('Время выполнения :', stop - start)
    # with Pool(5) as p:
    #     print(p.map(f, [1, 2, 3]))