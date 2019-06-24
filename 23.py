vx=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in b:
    a.append(i)
    print(max(a),end=' ')
