def toh(n,A,C,B):
    if n==1:
        print("move disk 1 from",A,"to",C)
        return
    else:
        toh(n-1,A,B,C)
        print("move disk",n,"from",A,"to",C)
        toh(n-1,B,C,A)
toh(4,'A','C','B')