n = int(input())
nums = set(range(2,n))

for x in range(2,n):
    nums -= set(range(x*2,n,x))

nums = sorted(nums)

print(nums)

