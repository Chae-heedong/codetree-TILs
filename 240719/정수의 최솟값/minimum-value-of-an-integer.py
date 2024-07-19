def findmin(a):
    b=a.split()
    k=int(b[0])
    for i in b:
        j=int(i)
        if k>j:
            k=j
    return k

num=input()
print(findmin(num))