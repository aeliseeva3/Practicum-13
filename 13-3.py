sladkoezhkin_products = set(input().split())
friends_count = int(input())
friends_products = set()

for _ in range(friends_count):
    friends_products |= set(input().split())

print(len(sladkoezhkin_products - friends_products))

