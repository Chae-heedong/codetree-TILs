n = int(input())
arr = list(map(int, input().split()))


# 맨앞값 추출. 크면 저장 아니면 버림. null이면 끝

def f(a):
    try:
        k=arr[0]
        if k>a:
            arr.remove(arr[0])
            return f(k)
        else:
            arr.remove(arr[0]) #remove로 리스트 삭제하는거 알아두기 
            return f(a)
    except: #arr[]이 비었을 때 종료
        return a
    
print(f(0))