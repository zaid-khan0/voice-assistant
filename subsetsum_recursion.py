def subsetsum(l,s,n):
    if s==0:
        return True
    if n==0:
        return False
    elif l[n-1]<=s:
        return subsetsum(l,s-l[n-1],n-1) or subsetsum(l,s,n-1)
    else:
        return subsetsum(l,s,n-1)
l=list(map(int,input().split()))
s=int(input())
print(subsetsum(l,s,len(l)))