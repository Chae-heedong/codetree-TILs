a=input().split()
b=input().split()

if "M" in a and int(a[0])>=19:
    print(1)
elif "M" in b and int(b[0])>=19:
    print(1)
else:
    print(0)