R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]
cntw=0 # W개수
ways=0 #가능한 경우의 수 
# 양끝 같은색 W-R-W W-R-W-R-W 2 4가능
# 양끝 다른색 W-R 같이 홀수가능

#WBWB BWBW만 가능
if grid[0][0]==grid[R-1][C-1]:
    cnt=0
else:
    if grid[0][0]=="B": #BWBW의 경우
        cnt=0
        for i in range(1,R):
            for j in range(1,C):
                #다음 W찾기
                if grid[i][j]=="W":
                    for p in range(i+1,R-1):
                        for q in range(j+1,C-1):
                            if grid[p][q]=="B":
                                cnt=cnt+1                           
    if grid[0][0]=="W": #WBWB의 경우
        cnt=0
        for i in range(1,R-2):
            for j in range(1,C-2):
                #다음 B찾기
                if grid[i][j]=="B":
                    for p in range(i+1,R-1):
                        for q in range(j+1,C-1):
                            if grid[p][q]=="W":
                                cnt=cnt+1
print(cnt)
#무조건 대각선으로 넘기때문에 처음껀 R-2 C-2 두번째껀 R-1 C-1
# 1행, 1열은 무조건 무의미