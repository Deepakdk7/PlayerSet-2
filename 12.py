ax=list(map(int,input().split()))
a=list(map(int,input().split()))
k=ax[1]
for i in range(0,k):
    a=[a[-1]]+a[:-1]
print(*a)
