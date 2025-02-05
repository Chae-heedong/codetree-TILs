N = input()
arr=[]
firstnum=0

for i in N:
    arr.append(int(i))

arr=arr[::-1]

for i in range(0,len(arr)):
    firstnum=firstnum+arr[i]*2**i

secondnum=firstnum*17
output=""

while True:
    if secondnum<2:
        output=output+str(secondnum)
        break
    output=output+str(secondnum%2)
    secondnum=secondnum//2

print(output[::-1])
# Write your code here!