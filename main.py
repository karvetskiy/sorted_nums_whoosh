import time
import numpy as np


def getNumbers():
    a = np.loadtxt('input.csv', dtype='str')  # читаем из файла
    for i in range(len(a)):  # обрезаем "+79" в строках
        tmp = a[i]
        a[i] = tmp[3:]
    b = np.array(a, int)  # создаем массив с числами на основе первого
    return b


def makeOutput(a):
    tic = time.perf_counter()  # начало таймера
    a.sort()  # сортировка
    toc = time.perf_counter()  # конец таймера
    print(toc - tic)  # вывод времени сортировки
    b = np.array(['+7' + str(9000000000 + i) for i in a])  # создание массива с форматироваными номерами
    np.savetxt('output.csv', b, fmt='%s')  # запись в файл


def genNumbers():
    a = np.array(['+7' + str(9000000000 + i) for i in range(1000000000)])  # создаем массив(не очень эффективно по
                                                                           # памяти, но это лучшее, что я придумал)
    np.random.shuffle(a)  # перемешиваем
    np.savetxt('input.csv', a, fmt='%s')  # кидаем в файл


genNumbers()
makeOutput(getNumbers())
