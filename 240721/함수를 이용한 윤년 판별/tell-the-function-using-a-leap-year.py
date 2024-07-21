def leapyear(a):
    if a%4==0:
        if a%400==0:
            return True
        elif a%100==0:
            return False
        else:
            return True
    else:
        return False

a=int(input())
if leapyear(a):
    print("true")
else:
    print("false")