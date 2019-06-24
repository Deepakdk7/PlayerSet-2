ax=int(input())
c=[]
x=[]
z=[]
a=input().split()
for i in a:
    if i not in c:
        c.append(i)
for i in c:
    d=0
    for j in range(0,len(a)):
        if i==a[j]:
            d=d+1
    x.append(i)
    x.append(d)
    z.append(d)
v=sorted(z)
for i in range(0,len(x)):
    if x[i]==v[0]:
        print(x[i-1])
