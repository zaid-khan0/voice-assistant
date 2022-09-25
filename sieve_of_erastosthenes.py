l=[]
for i in range(9999999):
    l.append(i)
l[0]=0
l[1]=0
p=2
while(p*p<=len(l)):
    if p!=0:
        for i in range(p*2,len(l),p):
            l[i]=0
    p=p+1
for i in range(len(l)):
    if l[i]!=0:
        print(l[i],end=" ")