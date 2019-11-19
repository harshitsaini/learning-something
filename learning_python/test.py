import time
import multiprocessing as mp


def f(num, lk):

    with lk:
        num.value += 1
    # num += 1


if __name__ == '__main__':
    lk = mp.Lock()
    manager = mp.Manager()
    # num = mp.Value('i', 0)
    num = manager.Value('i', 0)
    # num.value = 0
    # num = 0
    for i in range(100):
        p = mp.Process(target=f, args=(num, lk))
        q = mp.Process(target=f, args=(num, lk))
        p.start()
        q.start()
        p.join()
        q.join()

    print(num.value)
    # print(num)
