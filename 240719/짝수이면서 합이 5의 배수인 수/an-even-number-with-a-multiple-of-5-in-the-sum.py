def myfunction(n):
    if n%2==0:
        m=str(n)
        l=int(m[0])+int(m[1])
        if l%5==0:
            return True
        else:
            return False
    else:
        return False

a=int(input())
if myfunction(a):
    print("Yes")
else:
    print("No")