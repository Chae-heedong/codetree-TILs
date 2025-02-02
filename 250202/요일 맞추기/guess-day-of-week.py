m1, d1, m2, d2 = map(int, input().split())
daylist=[31,28,31,30,31,30,31,31,30,31,30,31]
def daycount(m,d): #작년 12월 31일으로부터의 차이 계산 
    k=0
    if m==1:
        k=0
    else:
        for i in range(0,m-1):
            k=k+daylist[i]
    return k+d

res=daycount(m2,d2)-daycount(m1,d1) #날짜 차이 계산

if res%7==0:
    print("Mon")
elif res%7==1:
    print("Tue")
elif res%7==2:
    print("Wed")
elif res%7==3:
    print("Thu")
elif res%7==4:
    print("Fri")
elif res%7==5:
    print("Sat")
elif res%7==6:
    print("Sun")