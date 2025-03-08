n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

x2=x[::]
x2.sort()
score=0
scores=[]
for i in range (0,x2[-1]-k+1):
    for j in range(i,i+k):
        for p in range(0,k):
            if x[p]==j:
                if c[p]=='H':
                    score=score+2
                else:
                    score=score+1
    scores.append(score)
    score=0
scores.sort()
print(scores[-1]+1)