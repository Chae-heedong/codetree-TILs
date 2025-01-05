#피보나치 수열: 1,1,2,3 전꺼+전전꺼 f(n)=f(n-1)+f(n-2)
def f(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
a=int(input())
print(f(a))