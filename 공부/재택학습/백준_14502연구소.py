N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 2에 대해, 확산시 최소 범위 + 그 경로에 벽을 세울 경우, 상하좌우로 막히는 곳