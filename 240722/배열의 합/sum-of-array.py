a=[]
for i in range(4):
    k=input().split()
    a.append(k)
t=0
for i in range(4):
    for j in range(4):
        t=t+int(a[i][j])
    print(t)
    t=0