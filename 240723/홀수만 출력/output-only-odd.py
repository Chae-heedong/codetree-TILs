a, b=input().split()
a=int(a)
b=int(b)

if a%2==0:
    a=a+1
if b%2==1:
    b=b+1

for i in range(a,b,2):
    print(i, end=" ")