dx=int(input())
x=list(input())
for i in x:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        x.remove(i)
x=x[::-1]
for i in x:
    print(i,end="")
