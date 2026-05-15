from itertools import combinations


numbers = sorted(map(int, input().split()))
k = int(input())

for combo in combinations(numbers, k):
    print('{' + ', '.join(map(str, combo)) + '}')

