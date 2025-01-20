n = int(input())
nums = list(map(int, input().split()))
sum_=0
biggest=0

nums.sort()

# abcdef면 a+f, b+e, c+d중 젤 작은거. 끝값만 비교

while len(nums)>0:
    sum_=nums[0]+nums[-1]
    if biggest<sum_:
        biggest=sum_
    nums.remove(nums[0])
    nums.remove(nums[-1])

print(biggest)
    
