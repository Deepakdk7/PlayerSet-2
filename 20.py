ax=list(input())
c=[]
a=0
for i in ax:
    if ord(i)>26:
        a=ord(i)-26
        c.append(a+3)
    else:
        c.append(ord(i)+3)
for i in c:
    print(chr(i),end="")
