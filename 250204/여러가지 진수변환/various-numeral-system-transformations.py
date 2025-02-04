N, B = map(int, input().split())
arr=[]

while True:
    if N<B:
        arr.append(N)
        break
    arr.append(N%B)
    N=N//B

for i in arr[::-1]:
    print(i, end='')
# Write your code here!