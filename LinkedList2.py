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
buildlist2()
    