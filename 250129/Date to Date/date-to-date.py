m1, d1, m2, d2 = map(int, input().split())
daylist=(31,28,31,30,31,30,31,31,30,31,30,31)

#첫달
total=daylist[m1-1]-d1+1

#중간달은 통으로 계산
if m1+1<m2:
    for i in range(m1,m2-1):
        total=total+daylist[i]

#마지막달은 걍 d2더히면됨
total=total+d2

print(total)
