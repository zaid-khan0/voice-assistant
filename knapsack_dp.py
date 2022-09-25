def knapsack(w,p,wt,n):
    l=[[0 for j in range(wt+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(wt+1):
            if i==0 or j==0:
                l[i][j]=0
            elif w[i-1]<=j:
                l[i][j]=max(p[i-1]+l[i-1][j-w[i-1]],l[i-1][j])
            else:
                l[i][j]=l[i-1][j]
    return l
w=list(map(int,input().split()))
p=list(map(int,input().split()))
wt=int(input())
print(knapsack(w,p,wt,len(w)))