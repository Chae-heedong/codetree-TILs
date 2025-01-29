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

#동일월 고려
if m1==m2:
    total=total-daylist[m1-1]

#-고려
if m1>m2 or (m1==m2 and d1>d2):
    total=total-365

print(total)
