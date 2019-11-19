from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register('get_queue')
m = QueueManager(address=('localhost', 50000), authkey=b'abracadabra')
s = m.connect()
queue = m.get_queue()
print(queue.get('hello'))
