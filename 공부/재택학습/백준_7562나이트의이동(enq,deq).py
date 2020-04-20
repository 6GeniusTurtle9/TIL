def knight_move(s1, s2, cnt):
    global front, rear
    rear += 1
    q[rear] = [s1, s2, cnt]
    while front != rear:
        front += 1
        cur1, cur2, cnt = q[front]
        if cur1 == e1 and cur2 == e2:
            return cnt-1
        else:
            for t in range(8):
                next1, next2 = cur1 + knight_dir[t][0], cur2 + knight_dir[t][1]
                if 0 <= next1 < L and 0 <= next2 < L:
                    if next1 == e1 and next2 == e2:
                        return cnt
                    elif chess[next1][next2] == 0:
                        chess[next1][next2] = cnt+1
                        rear += 1
                        q[rear] = [next1, next2, cnt+1]
    return 0

for tc in range(1, int(input())+1):
    L = int(input())
    chess = [[0]*L for _ in range(L)]
    s1, s2 = list(map(int, input().split()))
    e1, e2 = list(map(int, input().split()))
    knight_dir = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,2), (-1,-2)]
    cnt = 1
    q = [0]*(1000000)
    front, rear = -1, -1
    print(knight_move(s1, s2, cnt))