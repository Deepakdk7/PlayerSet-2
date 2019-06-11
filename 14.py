sx=int(input())
ax=list(input())
for i in ax:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        ax.remove(i)
ax=ax[::-1]
for i in ax:
    print(i,end="")
