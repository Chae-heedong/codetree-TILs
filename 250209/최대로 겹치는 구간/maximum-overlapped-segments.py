n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
lists=[]

for i in range(200):
    lists.append(0)

for i in range(0,n):
    a=segments[i][0]+100
    b=segments[i][1]+100
    for j in range(a-1,b):
        lists[j]=lists[j]+1

lists.sort()

print(lists[-1])