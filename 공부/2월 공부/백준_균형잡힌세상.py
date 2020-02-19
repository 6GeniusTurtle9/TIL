
while True:
    sen = list(input())
    result = "yes"
    s = []

    if sen[0] == '.':
        break

    else:
        for i in sen:
            if i == "(" or i == "[":
                s.append(i)

            elif i == ")":
                if len(s) != 0 and s[-1] != "(":
                    result = 'no'
                    break
                elif len(s) != 0 and s[-1] == "(":
                    s.pop()

            elif i == ']':
                if len(s) != 0 and s[-1] != '[':
                    result = 'no'
                    break
                elif len(s) != 0 and s[-1] == '[':
                    s.pop()
    if len(s) != 0:
        result = 'no'

    print(result)