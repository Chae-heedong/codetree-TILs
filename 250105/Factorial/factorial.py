N = int(input())

# 팩토리얼이 f(n)이면 f(n)=f(n-1)*n

def f(n):
    if n==1:
        return 1
    elif n==0:
        return 1 #팩토리얼 정의상 0팩토리얼이 1임을 고려
    else:
        return n*f((n-1))

print(f(N))