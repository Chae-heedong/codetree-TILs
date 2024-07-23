a=input().split()
b=input().split()

if "M" in a or "M" in b:
    print(1)
elif int(a[0])>=19 or int(b[0])>=19:
    print(1)
else:
    print(0)