a = input()
A=[]
cnt=0
k=len(a)
for b in a:
    A.append(b)

for i in range(0,k-1): #맨끝은 항상 불가->무조건 배제
    if A[i]=='(': #(찾으면 앞에 있는 )개수 카운트
        for j in range(i+1,k):
            if A[j]==')':
                cnt=cnt+1

print(cnt)
