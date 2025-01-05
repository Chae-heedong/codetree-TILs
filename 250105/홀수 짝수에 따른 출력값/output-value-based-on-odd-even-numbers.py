N = int(input())

#2씩 빼서 더하기. 홀수면 1에서 종료 짝수면 2에서 종료 f(n)=f(n-2)+n
# Write your code here!

def f(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return n+f(n-2)

print(f(N))
