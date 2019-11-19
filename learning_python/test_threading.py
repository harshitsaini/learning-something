# import threading

# from pprint import pprint


# # output = dict({
# #     "active_count": threading.active_count(),
# #     "current_thread": threading.current_thread(),
# #     "thread_ident": threading.get_ident(),
# #     "thread_enumerate": threading.enumerate(),
# #     "main_thread": threading.main_thread(),
# #     "stack_size": threading.stack_size(4096*32),
# #     "timeout_max": threading.TIMEOUT_MAX
# # }
# # )

# # pprint(output)
# # print("\n")
# # pprint(output['current_thread'].__dict__)


# # mydata = threading.local()
# # mydata.x = 7

# t1 = threading.Thread(name = "some_thread", daemon=False)
# print(t1.isDaemon())
# print(t1.setDaemon(daemonic=True))
# print(t1.isDaemon())

# from threading import Semaphore, BoundedSemaphore

# # Usually, you create a Semaphore that will allow a certain number of threads
# # into a section of code. This one starts at 5.
# s1 = Semaphore(5)

# # When you want to enter the section of code, you acquire it first.
# # That lowers it to 4. (Four more threads could enter this section.)
# print(s1._value)
# s1.acquire()
# print(s1._value)
# # Then you do whatever sensitive thing needed to be restricted to five threads.

# # When you're finished, you release the semaphore, and it goes back to 5.
# s1.release()
# print(s1._value)

# # That's all fine, but you can also release it without acquiring it first.
# s1.release()

# # The counter is now 6! That might make sense in some situations, but not in most.
# print(s1._value)  # => 6

# # # If that doesn't make sense in your situation, use a BoundedSemaphore.

# # s2 = BoundedSemaphore(5)  # Start at 5.

# # s2.acquire()  # Lower to 4.

# # s2.release()  # Go back to 5.

# # try:
# #     s2.release()  # Try to raise to 6, above starting value.
# # except ValueError:
# #     print('As expected, it complained.')


# from threading import Timer

# def hello():
#     print("hello, world")


# t = Timer(3.0, hello)
# t.start()  # after 30 seconds, "hello, world" will be printed

# import time
# from concurrent.futures import ThreadPoolExecutor


# def multithreading(func, args, workers):
#     with ThreadPoolExecutor(workers) as ex:
#         res = ex.map(func, args)
#     return list(res)


# def cpu_heavy(x):
#     print('I am', x)
#     count = 0
#     for i in range(5*(10**8)):
#         count += i


# n_jobs = 4

# marker = time.time()
# for i in range(n_jobs): cpu_heavy(i)
# print("Serial spent", time.time() - marker)
# marker = time.time()
# multithreading(cpu_heavy, range(n_jobs), 4)
# print("Multithreading spent", time.time() - marker)

import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

urls = ['http://www.discovertunisia.com',
        'http://whc.unesco.org/en/list/38',
        'https://www.youtube.com/watch?v=sHORcz5nqIc',
        'https://www.youtube.com/watch?v=dyHjCwKoNn8'
        'http://www.tourismtunisia.com/10-adventurous-things-to-do-in-tunisia/',
        'http://wowtravel.me/top-10-things-to-do-in-tunisia/',
        'http://en.wikipedia.org/wiki/Tataouine',
        'http://en.wikipedia.org/wiki/Carthage',
        'http://en.wikipedia.org/wiki/Hannibal',
        'http://www.discovertunisia.com',
        'http://whc.unesco.org/en/list/38',
        'https://www.youtube.com/watch?v=sHORcz5nqIc',
        'https://www.youtube.com/watch?v=dyHjCwKoNn8'
        'http://www.tourismtunisia.com/10-adventurous-things-to-do-in-tunisia/',
        'http://wowtravel.me/top-10-things-to-do-in-tunisia/',
        'http://en.wikipedia.org/wiki/Tataouine',
        'http://en.wikipedia.org/wiki/Carthage',
        'http://en.wikipedia.org/wiki/Hannibal'
        ]


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def load_url(x):
    # print('I am', x)
    import os
    print(os.getpid())
    with urllib.request.urlopen(urls[x], timeout=20) as conn:
        return conn.read()


n_jobs = len(urls)

marker = time.time()
for i in range(n_jobs):
    load_url(i)
print("Serial spent", time.time() - marker)

for n_threads in [4, 8, 16]:
    marker = time.time()
    multithreading(load_url, range(n_jobs), n_threads)
    print("Multithreading {} spent".format(n_threads), time.time() - marker)
