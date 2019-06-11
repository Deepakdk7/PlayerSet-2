ax=int(input())
s=r=0
while ax!=0:
    r=ax%10
    s=s+r**2
    ax=ax//10
print(s)
