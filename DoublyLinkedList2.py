from DoublyLinkedList import DoublyLinkedList

def buildListRight(val):
    assert len(val)>0,"no element"
    a=DoublyLinkedList(val[0])
    for i in range(1,len(val)-1):
        a.insertright(val[i])
        a=a.right
    return a

def buildListLeft(val):
    assert len(val)>0,"no element"
    a=DoublyLinkedList(val[0])
    for i in range(1,len(val)-1):
        a.insertleft(val[i])
        a=a.left
    return a

