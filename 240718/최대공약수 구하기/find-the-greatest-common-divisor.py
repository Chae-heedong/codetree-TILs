a,b=input().split()
a=int(a)
b=int(b)
c=0
d=0

while c<a and c<b:
    c=c+1
    if a%c==0 and b%c==0:
        d=c
print(d)