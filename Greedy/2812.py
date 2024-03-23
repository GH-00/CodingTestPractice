import sys
input = sys.stdin.readline

N,K = map(int,input().split())
s = input()

arr = []
for word in s:
    while arr and arr[-1] < word and K>0:
        arr.pop()
        K -= 1
    arr.append(word)

if K>0:
    print(''.join(map(str,arr[:-K])))

else:
    print(''.join(map(str,arr)))