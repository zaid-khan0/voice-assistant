l=[5,3,8,7,9,1]
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
for i in range(len(l)):
    print(l[i],end=" ")