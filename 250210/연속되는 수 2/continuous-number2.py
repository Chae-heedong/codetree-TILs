n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
cnt=0
biggestcnt=0
prenum=""
for i in arr:
    if biggestcnt<cnt:
            biggestcnt=cnt #가장 큰 카운트 입력
    if i==prenum:
        cnt=cnt+1
    else:
        cnt=1 #리셋
    prenum=i

print(biggestcnt)
