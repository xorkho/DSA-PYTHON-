class Queue:
    def __init__(self):
        self._qlist=list()
    
    def isEmpty(self):
        return len(self._qlist)==0
    
    def __len__(self):
        return len(self._qlist)
    
    def Enqueue(self,item):
        self._qlist.append(item)
    
    def Dequeue(self):
        assert not self.isEmpty(),"cant dequeue from an empty queue"
        self._qlist.pop(0)

q=Queue()
q.Enqueue(4)
q.Enqueue(5)
q.Enqueue(6)
q.Enqueue(7)
q.Enqueue(8)
print(q._qlist)