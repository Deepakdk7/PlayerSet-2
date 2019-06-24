ax=list(input())
a=[]
e=[]
d=[]
c=w=0
for i in range(0,len(ax)):
    if ax[i] not in a:
        a.append(ax[i])
for i in a:
    c=0
    for j in range(0,len(ax)):
        if i==ax[j]:
            c=c+1
    d.append(i)
    d.append(c)
    e.append(c)
w=max(e)
for i in range(0,len(d)):
    if d[i]==w:
        print(d[i-1])
