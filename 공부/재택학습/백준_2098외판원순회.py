import copy

def STP(cur, n, toll):
    global min_toll

    if toll > min_toll: # 시간 줄이려고
        return
    
    if n == N-1 and W[cur][start] != 0:    # 모든 곳을 방문한 뒤에 처음 자리로 올 수 있다면
        toll += W[cur][start]
        tmp = toll
        if min_toll > tmp:
            min_toll = tmp
    else:
        for next in range(N):
            if W[cur][next] != 0 and visited[next] == 0:    # 길이 있으며, 방문하지 않은 곳으로
                visited[next] = 1
                STP(next, n+1, toll+W[cur][next])
                visited[next] = 0

N = int(input())
W = [list(map(int, input().split()))for _ in range(N)]

visit = [0]*N
real_toll = 1000000000000000

for start in range(N):
    visited = copy.deepcopy(visit)
    tolls = []
    visited[start] = 1
    toll = 0
    min_toll = 1000000000000
    STP(start, 0, toll)
    visited[start] = 0
    if real_toll > min_toll:
        real_toll = min_toll

print(real_toll)