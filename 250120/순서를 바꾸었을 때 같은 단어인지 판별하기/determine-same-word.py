word1 = input()
word2 = input()
w1=[]
w2=[]

for i in word1: #쪼개서 넣기
    w1.append(i)
for i in word2:
    w2.append(i)

w1.sort()
w2.sort()

if w1==w2:
    print("Yes")
else:
    print("No")
# 정렬해서 같아지면 Yes 아니면 No
