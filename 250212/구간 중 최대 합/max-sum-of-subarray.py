n, k = map(int, input().split())
arr = list(map(int, input().split()))
numlist=[]

for i in range(2,n):
    numlist.append(arr[i-2]+arr[i-1]+arr[i])

numlist.sort()
print(numlist[-1])