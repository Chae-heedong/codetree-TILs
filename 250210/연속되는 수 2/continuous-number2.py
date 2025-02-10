n = int(input())
arr = [int(input()) for _ in range(n)]
cnt=1
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

if arr[0]==arr[-1]:
    biggestcnt=biggestcnt+1 #다 같은수면 1개 덜셈 

print(biggestcnt)
