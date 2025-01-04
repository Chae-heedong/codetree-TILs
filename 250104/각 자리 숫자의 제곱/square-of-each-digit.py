N = int(input())

def fk(n):
    if n<10:
        return n**2
    else:
        return fk(n//10)+(n%10)**2

print(fk(N))
# Write your code here!