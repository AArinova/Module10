from multiprocessing import Pool
from datetime import datetime

def read_info(name):

    with open(name, "r", encoding='utf-8') as file:
        line = file.readline()
        while line:
            line = file.readline()

if __name__ == '__main__':

    fnames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    start = datetime.now()
    for fname in fnames:
        read_info(fname)
    stop = datetime.now()
    print('Время выполнения при линейном вызове:', stop - start)

    start = datetime.now()
    with Pool(4) as pool:
        pool.map(read_info, fnames)
    stop = datetime.now()
    print('Время выполнения при мультипроцессорном вызове:', stop - start)



