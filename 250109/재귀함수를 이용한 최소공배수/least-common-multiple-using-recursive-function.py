n = int(input())
arr = list(map(int, input().split()))
p=1
#f(a,b)=ab 최소공배수 
#g(x)=arr[x]와 g(x+1)의 최소공배수 출력. 다 구하면 에러이므로 try 이용

def f(a,b):
    i=1
    j=1
    while i<=a and i<=b:
        if a%i==0 and b%i==0:
            j=j*i
        i=i+1
    return a*b/j

def g(x):
    try:
        return f(arr[x],g(x+1))
    except: 
        return 1


print(int(g(0)))
