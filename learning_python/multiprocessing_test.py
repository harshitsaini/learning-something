from multiprocessing import Pool


def f(x):
    return x*x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))


# # from multiprocessing import Process


# # def f(name):
# #     print('hello', name)


# # if __name__ == '__main__':
# #     p = Process(target=f, args=('bob',))
# #     p.start()
# #     p.join()


# # from multiprocessing import Process
# # import os


# # def info(title):
# #     print(title)
# #     print('module name:', __name__)
# #     print('parent process:', os.getppid())
# #     print('process id:', os.getpid(), end="\n\n")


# # def f(name):
# #     info('function f')
# #     print('hello', name)


# # # if __name__ == '__main__':
# # info('main line')
# # p = Process(target=f, args=('bob',))
# # p.start()
# # p.join()


# # import multiprocessing as mp


# # def foo(q):
# #     q.put('hello')


# # if __name__ == '__main__':
# #     mp.set_start_method('spawn')
# #     q = mp.Queue()
# #     p = mp.Process(target=foo, args=(q,))
# #     p.start()
# #             print(q.get())
# #     p.join()


# # import multiprocessing as mp


# # def foo(q):
# #     q.put('hello')


# # if __name__ == '__main__':
# #     ctx = mp.get_context('spawn')
# #     q = ctx.Queue()
# #     p = ctx.Process(target=foo, args=(q,))
# #     p.start()
# #     print(q.get())
# #     p.join()

# # from multiprocessing import Process, Queue


# # def f(q):
# #     q.put([42, None, 'hello'])


# # def g(q):
# #     q.put([69, None, 'whatup'])


# # if __name__ == '__main__':
# #     q = Queue()
# #     p1 = Process(target=f, args=(q,))
# #     p2 = Process(target=g, args=(q,))
# #     p1.start()
# #     p2.start()
# #     print(q.get())    # prints "[42, None, 'hello']"
# #     print(q.get())
# #     p1.join()
# #     p2.join()

# # from multiprocessing import Process, Pipe


# # def f(conn):
# #     # conn.send([42, None, 'hello'])
# #     # conn.send([69, None, 'whatup'])
# #     print(conn.recv()+1)
# #     conn.close()


# # if __name__ == '__main__':
# #     parent_conn, child_conn = Pipe()
# #     p = Process(target=f, args=(child_conn,))
# #     p.start()
# #     # print(parent_conn.recv())   # prints "[42, None, 'hello']"
# #     # print(parent_conn.recv())
# #     parent_conn.send(10)
# #     p.join()

# from multiprocessing import Process, Lock


# def f(l, i):
#     l.acquire()
#     try:
#         print('hello world', i)
#     finally:
#         l.release()


# if __name__ == '__main__':
#     lock = Lock()

#     for num in range(100):
#         p = Process(target=f, args=(lock, num))
#         p.start()
#         p.join()

# from multiprocessing import Process, Value, Array


# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]


# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))

#     p = Process(target=f, args=(num, arr))
#     p.start()
#     p.join()

#     print(num.value)
#     print(arr[:])


# from multiprocessing import Process, Manager


# def f(d, l):
#     d[1] = '1'
#     d['2'] = 2
#     d[0.25] = None
#     l.reverse()


# if __name__ == '__main__':
#     with Manager() as manager:
#         d = manager.dict()
#         l = manager.list(range(10))

#         p = Process(target=f, args=(d, l))
#         p.start()
#         p.join()

#         print(d)
#         print(l)


# import multiprocessing
# import time
# import signal


# p = multiprocessing.Process(target=time.sleep, args=(1000,))
# print(p, p.is_alive())
# p.start()
# print(p, p.is_alive())
# # p.terminate()
# p.kill()
# time.sleep(0.1)
# print(p, p.is_alive())
# print(p.exitcode == -signal.SIGTERM)
# print(p.exitcode == -signal.SIGKILL)
# print(p.exitcode, -signal.SIGTERM, -signal.SIGKILL)


import array
from multiprocessing import Pipe
a, b = Pipe()
a.send([1, 'hello', None])
b.recv()

b.send_bytes(b'thank you')
a.recv_bytes()

arr1 = array.array('i', range(5))
arr2 = array.array('i', [0] * 10)
a.send_bytes(arr1)
count = b.recv_bytes_into(arr2)
assert count == len(arr1) * arr1.itemsize
print(arr2)
