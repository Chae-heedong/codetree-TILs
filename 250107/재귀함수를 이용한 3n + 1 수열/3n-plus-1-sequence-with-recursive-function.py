n = int(input())

# f(n)이 n의 칸트개수면 n짝-> f(n)=f(n/2)+1 홀->f(n)=f(n*3+1)+1 

def f(x):
    if x==1:
        return 0
    elif x%2==0:
        return f(x/2)+1
    else:
        return f(x*3+1)+1

print(f(n))