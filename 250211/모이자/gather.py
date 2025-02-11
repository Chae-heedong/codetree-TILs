n = int(input())
A = list(map(int, input().split()))
numlist=[]
num=0

for i in range(0,n): #점이 i 일 때의 거리합
    for j in range(0,n):
        num=num+abs(i-j)*A[j]
    numlist.append(num)
    num=0 #리셋


numlist.sort()
print(numlist[0])