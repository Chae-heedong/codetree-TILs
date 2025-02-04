n = int(input())
resultt=[]
while True:
    if n<2:
        resultt.append(n)
        break
    resultt.append(n%2)
    n=n//2

for i in resultt[::-1]:
    print(i,end='')

# Write your code here!