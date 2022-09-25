import csv
x=[]
y=[]
with open('file.txt','r') as f:
    data=csv.reader(f)
    for col in data:
        x.append(col[0])
        y.append(col[1])
print(x)
print(y)