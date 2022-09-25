def knapsack(w,p,wt,n):
    if wt==0 or n==0:
        return 0
    elif w[n-1]<=wt:
        return max(p[n-1]+knapsack(w,p,wt-w[n-1],n-1),knapsack(w,p,wt,n-1))
    elif w[n-1]>wt:
        return knapsack(w,p,wt,n-1)
w=list(map(int,input().split()))
p=list(map(int,input().split()))
wt=int(input())
print(knapsack(w,p,wt,len(w)))