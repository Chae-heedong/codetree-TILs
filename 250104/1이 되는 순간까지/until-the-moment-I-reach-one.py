N = int(input())

def fx(n):
    if n==1:
        return 0
    elif n%2==0:
        return fx(n/2)+1
    elif n%2==1:
        return fx(n//3)+1

print(fx(N))