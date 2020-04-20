di = [-2, -2, -1, 1, 2, 2, 1, -1]
dj = [-1, 1, 2, 2, 1, -1, -2, -2]
def knight_move(s1, s2, cnt):
    q = []
    q.append((s1, s2, cnt))
    chess[s1][s2] = 1
    while q:
        cur1, cur2, cnt = q.pop(0)
        if cur1 == e1 and cur2 == e2:
            return cnt
        else:
            for t in range(8):
                next1 = cur1 + di[t]
                next2 = cur2 + dj[t]
                if 0 <= next1 < L and 0 <= next2 < L and chess[next1][next2] == 0:
                    chess[next1][next2] = 1
                    q.append((next1, next2, cnt+1))

for tc in range(1, int(input())+1):
    L = int(input())
    chess = [[0]*L for _ in range(L)]
    s1, s2 = list(map(int, input().split()))
    e1, e2 = list(map(int, input().split()))
    cnt = 0
    if s1 == e1 and s2 == e2:
        print(0)
    else:
        print(knight_move(s1, s2, cnt))