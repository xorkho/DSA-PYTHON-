from LinkedList import ListNode
class Stack:
    def __init__(self):
        self.top=None

    def isEmpty(self):
        return self.top is None

    def push(self,val):
        x=ListNode(val)
        x.next=self.top
        self.top=x
    
    def pop(self):
        assert not self.isEmpty(),"stack is empty"
        x=self.top.data
        self.top=self.top.next
        return x
