# Enqueue, Dequeue, //size, empty, front

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class LinkedListQueue(): 
    def __init__(self): 
        self.front = None 
        self.rear = None 
    
    def enqueue(self, data): 
        new_node = Node(data) 
        if self.front is None: 
            self.front = new_node 
            self.rear = new_node 
        else: 
            self.rear.next = new_node 
            self.rear = self.rear.next 

    def dequeue(self): 
        dequeue_object = None 
        if self.isEmpty(): 
            print("Queue is Empty") 
        else: 
            dequeue_object = self.front.data 
            self.front = self.front.next 

            if self.front is None: 
                self.rear = None 
            return dequeue_object 

    def peek(self): 
        front_object = None 

        if self.isEmpty(): 
            print("Queue is Empty") 
        else: 
            front = self.front.data
            return front_object

    def isEmpty(self): 
        is_empty = False 
    
        if self.front is None: 
            is_empty = True 
        return is_empty


# from typing import Deque

# class Queue():
#     def __init__(self):
#         self.myQueue = []

#     def Enqueue(self, data):
#         self.myQueue.append(data)

#     def Dequeue(self):
#         if len(self.myQueue) == 0:
#             return
#         else:
#             return self.myQueue.pop(0)

# q = Queue()

# q.Enqueue(1)
# q.Enqueue(2)
# q.Enqueue(3)

# print(q.Dequeue())
# print(q.Dequeue())

