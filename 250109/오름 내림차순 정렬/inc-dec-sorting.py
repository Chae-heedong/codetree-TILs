n = int(input())
nums = list(map(int, input().split()))

def f(x):
    for i in x:
        print(i, end=' ')
    print()

nums.sort() #오름차순(커지게끔) 정렬
f(nums)

nums.sort(reverse=True)
f(nums)
# Write your code here!
