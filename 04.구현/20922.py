# 투포인터 정리하기
import sys
input=sys.stdin.readline

N,K=map(int,input().split())

L=list(map(int,input().split()))

start=0 ; end=1

A=[0]*100001

A[L[start]]+=1 ; count=1 ; answer=0
while end<N:
    if A[L[end]]<K:
        A[L[end]]+=1
        count+=1
        end+=1

    elif A[L[end]]>=K:
        A[L[start]]-=1
        start+=1
        count-=1
    answer=max(answer,count)

print(answer)