'''
    Autor: Reyna Yazmin Ríos Martínez
    Fecha: 09 de nov de 2023
    Descripción: Colas alias FIFO: parte 2
'''
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.insert(0, item)  

    def get(self):
        if not self.items:
            raise QueueError("Cola vacia")  
        return self.items.pop()  
    def is_empty(self):
        return not bool(self.items)  


q = Queue()
q.put(1)
q.put("perro")
q.put(False)

try:
    print(q.get())  
    print(q.get())  
    print(q.get())  
    print(q.get())  
except QueueError as e:
    print(e)  

print(q.is_empty())  