n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

x2=x[::]
x2.sort()
scores=[]

for i in range (1,10000-k):
    score=0
    #0부터 끝-k 까지
    for j in range(i,i+k+1):
        if j in x:
            p=x.index(j)

            if c[p]=='H':
                score=score+2
            else:
                score=score+1
    scores.append(score)

scores.sort(reverse=True)
print(scores[0])
