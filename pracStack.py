from stack import Stack
s=Stack()
x=4
z=0
y=x+1
s.push(y)
s.push(y+1)
s.pop()
x=y+1
s.push(x)
s.push(z)
while(not(s.is_empty())):
    s.pop()
    print(z)
print("x=",x)
print("y=",y)
print("z=",z)
