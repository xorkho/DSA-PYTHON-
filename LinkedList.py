class ListNode:
    def __init__(self,value):
        self.data=value
        self.next=None

    def insert(self,value):
        n=ListNode(value)
        n.next=self.next
        self.next=n

    def delete(self):
        item=None
        if self.next is not None:
            temp=self.next
            item=temp.data
            self.next=temp.next
        return item

    def __len__(self):
        a=self
        i=0
        while a is not None:
            i+=1
            a=a.next
        return i
    
    def search(self,target):
        a=self
        if a.data==target:
            return [True,None,a]
        b=a.next
        while b is not None and b.data!=target:
            a=a.next
            b=b.next
        return [b is not None,a,b]
    
    def insafter(head,x,val):
        res=head.search(x)
        if res[0]==True:
            res[2].insert(val)

    def insbefore(head,x,val):
        res=head.search(x)
        if res[0]==True:
            if res[2] is head:
                new=ListNode(val)
                new.next=head
                head=new
            else:
                res[1].insert(val)
        return head

    def delnode(head,x):
        res=head.search(x)
        if res[0]==True:
            if res[2] is head:
                head=head.next
            else:
                res[1].delete()
        return head
    

# def BuildList(lst):
#     assert len(lst)>0,"no element"
#     head=ListNode(lst[0])
#     b=head
#     for i in range(1,len(lst)):
#         b.insert(lst[i])
#         b=b.next
#     return head


# node1=ListNode(10)
# node2=ListNode(20)
# node3=ListNode(30)
# node4=ListNode(40)

# node1.next=node2
# node2.next=node3
# node3.next=node4
# head=node1
# current=head

# # node2.insert(80) 
# # node1.delete() 

# current = head.insbefore(20,60)     #INSERT BEFORE A SPECIC NODE

# current=head.delnode(10)  #DELETE THE SPECIFIC NODE

# current=BuildList([4,6,7,8])
# while current is not None:
#     print(current.data,end="--->")
#     current=current.next

# length_of_list = len(head)
# print("Length of the list:", length_of_list)  //len of nodes

# x=head.search(30 )  //SEARCHIN SPECIFIC NODE
# print(x)