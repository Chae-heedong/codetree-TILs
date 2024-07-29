a=input().split()
if a[1]=="*":
    print(f"{a[0]} * {a[2]} = {int(a[0])*int(a[2])}")
elif a[1]=="+":
    print(f"{a[0]} + {a[2]} = {int(a[0])+int(a[2])}")
elif a[1]=="-":
    print(f"{a[0]} - {a[2]} = {int(a[0])-int(a[2])}")
elif a[1]=="/":
    print(f"{a[0]} / {a[2]} = {int(a[0])/int(a[2])}")