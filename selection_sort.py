l=[14,46,43,27,57,41,45,21,70]
for i in range(len(l)):
    min=i
    for j in range(i+1,len(l)):
        if l[min]>l[j]:
            min=j
    temp=l[i]
    l[i]=l[min]
    l[min]=temp
    print(l[i],end=" ")