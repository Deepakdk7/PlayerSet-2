ax=list(map(int,input().split()))
for i in range(1,(ax[0]*ax[1])+1):
    if i%ax[0]==0 and i%ax[1]==0:
        print(i)
        break
