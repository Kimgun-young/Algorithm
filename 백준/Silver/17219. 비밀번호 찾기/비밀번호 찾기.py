import sys

N, M = map(int, sys.stdin.readline().strip().split())

program = {}

for _ in range(N):
    site, password = map(str, sys.stdin.readline().strip().split())
    program[site] = password

for _ in range(M):
    site = sys.stdin.readline().strip()
    print(program[site])