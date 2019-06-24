ax=int(input())
a=[]
c=[]
for i in range(1,ax+1):
    for j in range(1,ax+1):
        if i*j==ax:
            a.append(i)
            a.append(j)
a=list(dict.fromkeys(a))
for i in a:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        c.append(i)
c.sort()
for i in c:
    if i!=1:
        print(i,end=' ')
