import itertools

def f(arr):
    summ = 0
    for i in range(N-1):
        if cities[arr[i]][arr[i+1]] == 0:
            summ += 1000000
        else:
            summ += cities[arr[i]][arr[i+1]]
    summ += cities[arr[-1]][arr[0]]
    return summ

N = int(input())
cities = [[0]+list(map(int, input().split())) for _ in range(N)]
cities.insert(0, [0]*(N+1))
nums = list(range(1,N+1))

combinations = list(itertools.permutations(nums, N))
result = 1000000
for combination in combinations:
    if f(combination) < result:
        result = f(combination)

print(result)