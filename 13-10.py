from itertools import combinations

nums = eval(input().split("=")[1].strip())
result = set()

for combo in combinations(nums, 3):
    if sum(combo) == 0:
        result.add(tuple(sorted(combo)))

print([list(trio) for trio in result])

