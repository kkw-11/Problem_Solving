# Enqueue, Dequeue, size, empty, front


from typing import Deque


class Queue():
    def __init__(self):
        self.myQueue = []

    def Enqueue(self, data):
        self.myQueue.append(data)

    def Dequeue(self):
        if len(self.myQueue) == 0:
            return
        else:
            return self.myQueue.pop(0)


q = Queue()

q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)

print(q.Dequeue())
print(q.Dequeue())




