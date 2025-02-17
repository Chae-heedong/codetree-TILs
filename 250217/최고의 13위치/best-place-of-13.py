n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt=0
cnts=[]

for i in range(0,n):
    for j in range(0,n-2):
        for k in range(j,j+3):
            cnt=cnt+grid[i][k]
            cnts.append(cnt)
        cnt=0

cnts.sort()

print(cnts[-1])