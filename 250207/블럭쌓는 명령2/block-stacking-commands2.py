n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]
lists=[]

for i in range(0,100):
    lists.append(0) #일단 0 100개 들어있는 리스트 형성
for i in commands:
    for j in range(i[0]-1,i[1]):
        lists[j]=lists[j]+1 #쌓은 개수 추가

lists.sort(reverse=True) #큰게 앞으로
print(lists[0])   