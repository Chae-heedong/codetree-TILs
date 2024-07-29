def onjuncount(a,b):
    cnt=0
    for i in range(a,b+1):
        j=str(i)
        if i%2==1 and j[-1]!="5" and (i%3!=0 or i%9==0):
            cnt=cnt+1
    return cnt
a, b=input().split()
a=int(a)
b=int(b)

print(onjuncount(a,b))