a,b=input().split()
a=int(a)
b=int(b)
c=0
d=0

while c<(a/2)+1 or c<(b/2)+1:
    c=c+1
    if a%c==0 and b%c==0:
        d=c

print(int(a*b/d))