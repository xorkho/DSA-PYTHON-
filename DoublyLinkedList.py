class DoublyLinkedList:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

    def insertright(self,value):
        p = self
        q = DoublyLinkedList(value)
        r = p.right
        q.right = r
        q.left = p
        p.right = q
        if r is not None:
            r.left=q

    def insertleft(self,val):
        p=self
        r=p.left
        q=DoublyLinkedList(val)
        q.left=r
        q.right=p
        p.left=q
        if r is not None:
            r.right=q

    def delete(self):
        # p q r
        q=self
        p=self.left
        r=self.right
        if p is not None:
            p.right=r
        if r is not None:
            r.left=p
        if p is None:
            return r
        return p

    def __len__(self):
        i=0
        a=self
        while a is not None:
            i+=1
            a=a.right
        a=self.left
        while a is not None:
            i+=1
            a=a.left
        return i

    def Traverse(self):
        a=self
        while a.left is not None:
            a=a.left
        print("Traversing....")
        while a is not None:
            print(a.data,end="")
            a=a.right
        print()

    def searh(self,target):
        a=self
        while (a is not None)and(a.data!=target):
            a=a.right
        if a is not None:
            return a
        a=self.left
        while (a is not None)and(a.data!=target):
            a=a.left
        return a
