ax=int(input())
a=[]
c=0
b=['a','a','b','i','k','l']
for i in range(0,ax):
    a.append(list(input()))
for i in a:
    s=sorted(i)
    if b==s:
        c=c+1
print(c)
