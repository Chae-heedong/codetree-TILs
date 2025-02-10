n = int(input())
A = list(map(int, input().split()))
lengthlist=[]
totallength=0
for i in A: 
    for j in A:
        totallength=totallength+abs(i-j)
    lengthlist.append(totallength)
    totallength=0 #넣고 다시 초기화

lengthlist.sort()

print(lengthlist[-1])