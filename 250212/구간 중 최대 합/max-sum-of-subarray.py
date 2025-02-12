n, k = map(int, input().split())
arr = list(map(int, input().split()))
numlist=[]
num=0
for i in range(k-1,n):
    for j in range(0,k):
        num=num+arr[i-j]


    numlist.append(num)
    num=0

numlist.sort()
print(numlist[-1])