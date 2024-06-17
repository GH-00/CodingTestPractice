import sys
input = sys.stdin.readline

n = int(input())

dict = {}
for i in range(n):
    name, action = map(str, input().split())
    dict[name] = action

names = []
for key, value in dict.items():
    if value == 'enter':
        names.append(key)

names.sort(reverse=True)

print(*names)