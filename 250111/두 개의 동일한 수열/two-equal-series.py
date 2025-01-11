n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
result_='Yes'

for i in range(0,n):
    if A[i]!=B[i]: #혼동주의 
        result_='No'

print(result_)
# Write your code here!