# stack1=[]
# stack2=[]
# k=1
# num="10200"
# for i in range(len(num)-1,-1,-1):
#     if i>k:
#         stack1.append(num[i])
#     else:
#         stack2.append(num[i])
# print(stack1)
# print(stack2)

# l=[3,4]
# l1=[3,4]
# # print(l==l1)
# s="Le"
# print(s.isupper())

# s="3[a2[c]]"
# s=[s[i] for i in range(len(s))]
# print("s".upper()=="S")

# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(2))

def combination(gro,mem) :
    if mem == gro or mem ==0:
        return 1
    else:
        return combination(gro-1,mem-1) + combination(gro-1,mem)
print(combination(6,5))

s="leetcode"
x=[i for i in s]
print(x)