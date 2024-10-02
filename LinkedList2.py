from LinkedList import ListNode
def BuildList(lst):
    assert len(lst)>0,"no element"
    head=ListNode(lst[0])
    b=head
    for i in range(1,len(lst)):
        b.insert(lst[i])
        b=b.next
    return head

def buildlist2():
    nums=[]
    while True:
        user_input=input("Enter a number or (Q) to quit").lower()
        if user_input == "q":
            break
        nums.append(user_input)

    current=BuildList(nums)
    while current is not None:
        print(current.data,end="--->")
        current=current.next
# buildlist2()

def instail(h,x):
    if h is None:
        return ListNode(x)
    a=h
    while a.next is not None:
        a=a.next
    new=ListNode(x)
    a.next=new
    return h
head=BuildList([1,2,3,4])
current=instail(head,5)
while current is not None:
    print(current.data,end="--->")
    current=current.next