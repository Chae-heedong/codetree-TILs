a, b, c = map(int, input().split())
d=a*b*c
# n의 자리수합=n//10의 자리수합+n%10
def f(x):
    if x<10:
        return x
    else:
        return f(x//10)+x%10

print(f(d))
