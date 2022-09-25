n=int(input("enter a number"))
a=0
b=0
c=1
for i in range(n):
    a=b+c
    c=b
    b=a
    print(a,end=" ")