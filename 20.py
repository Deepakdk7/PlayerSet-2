ax=list(input())
c=[]
a=0
for i in ax:
    if ord(i)+3>90:
        a=ord(i)+3
        c.append(a-26)
    else:
        c.append(ord(i)+3)
for i in c:
    print(chr(i),end="")
