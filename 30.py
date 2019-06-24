ax=input().split()
k=int(ax[2])
a=ax[0]
b=ax[1]
c=0
for i in range(0,len(ax[0])):
    if a[i]!=b[i]:
        c=c+1
if c==k:
    print('yes')
else:
    print('no')
