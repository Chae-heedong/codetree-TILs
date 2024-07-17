def nemo(a):
    a=int(a)
    aa=a
    b=0

    for i in range(a): #줄마다 출력
        for j in range(aa):
            b=b+1
            if b==10:
                b=1 #b값 정리
            print(b, end=" ")
        print()

k=input()
nemo(k)