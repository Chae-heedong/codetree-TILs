n = int(input())
arr = [int(input()) for _ in range(n)]
cnt=1 #처음 시작카운트
maxcnt=0
prenum=""

for i in arr:
    if prenum==i:
        cnt=cnt+1 #전의 숫자와 같으면 칸트추가 
    else:
        if maxcnt<cnt:
            maxcnt=cnt #신기록 등장시 저장
            cnt=1 #리셋
        else:
            cnt=1
    prenum=i

if maxcnt==1:
    maxcnt=0 #연속 없을때 

print(maxcnt)

# Write your code here!