string = input().rstrip()
bomb = list(input().rstrip())

qq = []
for i in range(len(string)):
    qq.append(string[i])
    if qq[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            qq.pop()
if qq:
    print(*qq, sep='')
else:
    print('FRULA')