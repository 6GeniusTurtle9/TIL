sentence = list(input())
alps = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result = {}
for alp in alps:
    for idx, char in enumerate(sentence):
        if alp == char:
            result[alp] = idx
            break
        else:
            result[alp] = -1
for val in result.values():
    print(val, end = " ")