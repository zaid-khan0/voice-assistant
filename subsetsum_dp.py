def subsetsum(l,s,n):
    dp=[[False for j in range(s+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if i==0:
                dp[i][j]=False
            if j==0:
                dp[i][j]=True
            elif l[i-1]<=j:
                dp[i][j]=dp[i-1][j-l[i-1]] or dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][s]
l=list(map(int,input().split()))
s=int(input())
print(subsetsum(l,s,len(l)))