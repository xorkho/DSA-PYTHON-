from Array import Array
class Queue:
    def __init__(self,maxsize):
        self._count=0
        self._front=0
        self._back=maxsize-1
        self._qarray=Array(maxsize)

    def isEmpty(self):
        return len(self._qarray)==0
    
    def __len__(self):
        return self._count
    
    def isFull(self):
        return self._count==len(self._qarray)
    
    def Enqueue(self,item):
        assert not self.isFull(),"cannot enqueue"
        maxsize=len(self._qarray)
        self._back=(self._back+1)%maxsize
        self._qarray[self._back]=item
        self._count+=1
    
    def Dequeue(self):
        assert not self.isEmpty(),"cannot dequeue"
        maxsize=len(self._qarray)
        item=self._qarray[self._front]
        self._front=(self._front+1)%maxsize
        self._count-=1
        return item
    
q=Queue(6)
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)
q.Enqueue(6)
