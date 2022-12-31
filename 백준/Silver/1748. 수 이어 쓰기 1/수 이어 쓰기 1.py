n = input()
answer = 0
for i in range(1,len(n)):
    answer += 9*10**(i-1)*i
answer += (int(n)-10**(len(n)-1)+1)*len(n)
print(answer)