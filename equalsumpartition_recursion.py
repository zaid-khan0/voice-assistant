def equalsum(l,s,n):
    if s==0:
        return True
    if n==0:
        return False
    elif l[n-1]<=s:
        return equalsum(l,s-l[n-1],n-1) or equalsum(l,s,n-1)
    else:
        return equalsum(l,s,n-1)
l=list(map(int,input().split()))
s=sum(l)
if s%2!=0:
    print(False)
else:
    print(equalsum(l,s//2,len(l)))