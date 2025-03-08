n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

x2=x[::]
x2.sort(reverse=True)
scores=[]

for i in range (1,x2[0]+1):
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
