import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

M, N = map(int, sys.stdin.readline().split())
tray = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

Q = deque()
for r in range(N):
    for c in range(M):
        if tray[r][c] == 1:
            Q.append((r, c))

while Q:
    r, c = Q.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and tray[nr][nc] == 0:
            tray[nr][nc] = tray[r][c] + 1
            Q.append((nr, nc))

day = 0
for row in tray:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit(0)
    day = max(day, max(row))

print(day - 1)
