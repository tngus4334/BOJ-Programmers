n = int(input())
n_list = list(map(int,input().split()))
search = int(input())
cnt = 0
for i in n_list:
    if i == search:
        cnt += 1
print(cnt)