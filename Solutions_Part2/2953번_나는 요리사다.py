import sys
a=[sum(list(map(int, sys.stdin.readline().split()))) for _ in range(5)]
print(a.index(max(a))+1, max(a))
