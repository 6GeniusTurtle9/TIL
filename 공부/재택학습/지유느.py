class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

def insertLast(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        lst.tail.next = new
        lst.tail = new
    lst.size += 1

def insertFirst(lst, new):
    if lst.head is None:    # 빈리스트이면
        lst.head = lst.tail = new
    else:                   # 빈리스트가 아니면
        new.next = lst.head
        lst.head = new
    lst.size += 1

# 임의의 위치 삽입
def insertAt(lst, idx, new):    # idx: 인덱스 값
    # 빈 리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst, new)
    # 마지막에 추가하는 경우, idx >= lst.size
    elif idx >= lst.size:
        insertLast(lst, new)
    # 중간에 추가하는 경우
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
        lst.size += 1

T = int(input())
for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    nums = list(map(int, input().split()))
    my_list = LinkedList()
    for i in range(len(nums)):
        insertLast(my_list, Node(nums[i]))

    for _ in range(m):
        idx, num = map(int, input().split())
        insertAt(my_list, idx, Node(num))

    cur = my_list.head
    for _ in range(l):
        cur = cur.next
    print('#{} {}'.format(tc, cur.data))

# 임의의 위치 삭제
def deleteAt(lst, idx):
    # 빈리스트이거나, idx == 0 첫번째 위치를 삭제할 경우
    if lst.head is None or idx == 0:
        deleteFirst(lst)
    # 마지막을 삭제하는 경우
    elif idx >= lst.size:
        deleteLast(lst)
    #중간에 삭제
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        lst.size -= 1











