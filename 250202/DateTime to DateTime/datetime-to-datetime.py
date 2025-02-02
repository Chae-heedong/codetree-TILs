a, b, c = map(int, input().split())

# -1 출력해야 할 상황 먼저 분리
totaltime=c-11+60*(b-11)+1440*(a-11)

if totaltime>=0:
    print(totaltime)
else:
    print(-1)
