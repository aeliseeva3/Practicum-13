from itertools import combinations


numbers = sorted(map(int, input().split()))

all_subsets = []
for num in range(len(numbers) + 1):
    for combo in combinations(numbers, num):
        all_subsets.append(list(combo))

for subset in all_subsets:
    print('{' + ', '.join(map(str, subset)) + '}')

