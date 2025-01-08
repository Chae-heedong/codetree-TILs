N = int(input())

# f(n)=f(n-1)+f(n//3)

def f(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return f(n-1)+f(n//3)

print(f(N))
