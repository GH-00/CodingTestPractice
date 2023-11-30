import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

import math

a = math.ceil(h / (n + 1))
b = math.ceil(w / (m + 1))
result = a * b
print(result)


