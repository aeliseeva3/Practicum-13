n = int(input())
courses = set(input().split())

for _ in range(n - 1):
    student_courses = set(input().split())
    courses &= student_courses

print(len(courses))

