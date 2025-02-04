binary = input()
arr=[]
total=0

for i in binary:
    arr.append(int(i))

arr=arr[::-1]

for i in range(0,len(arr)):
    total=total+arr[i]*2**i

print(total)
# Write your code here!