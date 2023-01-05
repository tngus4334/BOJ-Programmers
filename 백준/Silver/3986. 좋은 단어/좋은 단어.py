n= int(input())
answer = 0
for _ in range(n):
    s = input()
    stack = []
    for i in s:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
            
    if len(stack) == 0:
        answer += 1
print(answer)
