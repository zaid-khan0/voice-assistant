l=[3,8,47,92,1,5,2]
n=47
lb=0
ub=len(l)-1
for i in range(len(l)):
    mid=(lb+ub)//2
    if n==l[i]:
        print(f"{n} found at index {i}")
    else:
        if n<mid:
            lb=mid+1
        else:
            ub=mid-1
