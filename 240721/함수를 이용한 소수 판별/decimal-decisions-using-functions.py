def 소수찾기(k):
    j=round(k**0.5)+1
    if k==1:
        return False #1은 제외
    if k==2:
        return True #2는 짝수인 유일한 소수라 예외처리 필요
    for i in range(2,j): #뭐로라도 나눠지면 배제
        if k%i==0:
            return False
    return True #루트값보다 작은걸로 안나눠지면 끝 

a, b=input().split()

a=int(a)
b=int(b)
c=0

for i in range(a,b+1):
    if 소수찾기(i):
        c=c+i

print(c)