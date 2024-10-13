from LinkedList import ListNode
# Write an algorithm del_x(H, x) that accepts head pointer H to a linked list and deletes all nodes having x in the info field.
def del_x(H, x):
    # see if any initial nodes contain x
    while H is not None and H.data == x:
        H = H.next
    # see if there IS a list left
    if H is None:
        return H
    a = H
    b = a.next
    while b is not None:
        if b.data == x:
            a.next = b.next
            b = a.next
        else:
            a = a.next
            b = b.next
    return H


# Write an algorithm count_x(H, x) that accepts head pointer H to a linked list and returns the count of nodes having x in the info field.

def count_x(H, x):
    count=0
    # see if a list exists
    if H is None:
        return 0
    while H is not None and H.data==x:
        H=H.next
        count+=1

    current=H
    while current is not None:
        if current.data == x:
            count += 1
        current = current.next
    return count

# Write an algorithm del_tail(H) that accepts head pointer H to a linked list and removes its tail node.
def del_tail(H):
    if H is None or H.next is None:
        return None
    current=H
    while current.next.next is not None:
        current=current.next
    current.next=None
    return H
#QUES
def combine(L1,L2):
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    current=L1
    while current.next is not None:
        current=current.next
    current.next=L2
    return L1
#QUES
def sublist(H):
    if H is None:
        return [None,None]
    current=H
    while current is not None:
        if current.data<0:
            new_head=current.next
            current.next=None
            return [H,new_head]
        current=current.next
    return [H,None]

#QUES
# Write an algorithm insB4 tail(H, x) that accepts head pointer H to a linked list and inserts a node having info =
# x before the tail node.

def insB4Tail(head,x):
    current=head
    while current.next.next is not None:
        current=current.next
    new=ListNode(x)
    new.next=current.next
    current.next=new
    return head


def BuildList(lst):
    assert len(lst)>0,"no element"
    head=ListNode(lst[0])
    b=head
    for i in range(1,len(lst)):
        b.insert(lst[i])
        b=b.next
    return head
L1=BuildList([3,2,45,6,7,8])
lis1=insB4Tail(L1,10)
while lis1 is not None:
    print(lis1.data,end="--->")
    lis1=lis1.next

def bubblesort(H):
    if H == None: return  # nothing to sort
    if H.next == None: return  # the list has a single element, no need to sort
    # the linked list has more than two elements
    a = H
    done = None
    while a.next != done:
        b = a
        while b.next != None:
            if b.data > b.next.data:
                b.data, b.next.data = b.next.data, b.data
            if b.next.next == done:
                done = b.next
                break
            else:
                b = b.next
    return
