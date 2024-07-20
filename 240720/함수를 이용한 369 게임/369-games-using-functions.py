def numlist(a,b):
    j=[]
    for i in range(a,b+1):
        j.append(i)
    return j

def find369(a):
    b=str(a)
    if a%3==0:
        return True
    elif "3" in b or "6" in b or "9" in b:
        return True
    else:
        return False

a, b=input().split()
a=int(a)
b=int(b)
c=numlist(a,b)
d=0

for i in c:
    if find369(i):
        d=d+1

print(d)