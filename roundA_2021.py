T=int(input())
for i in range(1,T+1):
    n,k=map(int,input().split())
    s=input()
    count=0
    for j in range(n//2):
        if s[j]!=s[n-1-j]:
            count+=1
    print("case #",i,":",k-count)

