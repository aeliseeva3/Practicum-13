numbers = list(map(int, input().split()))
target = int(input())

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

if target in duplicates:
    print("Да")
else:
    print("Нет")

