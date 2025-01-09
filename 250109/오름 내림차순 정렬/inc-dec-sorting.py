n = int(input())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
print(nums)
nums.sort()
print(nums)
# Write your code here!
