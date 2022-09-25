def minsubsum(arr,s):
    print(arr[:len(arr)//2])
    mn=s
    for i in range(len(arr)//2):
        if arr[i]==True:
            mn=min(mn,s-2*i)
    print(mn)
def subsum(arr,s):
    dp=[[False for j in range(s+1)] for i in range(len(arr)+1)]
    for i in range(len(arr)+1):
        for j in range(s+1):
            if i==0:
                dp[i][j]=False
            if j==0:
                dp[i][j]=True
            elif arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    minsubsum(dp[len(arr)],s)
arr=[1,2,7]
subsum(arr,sum(arr))