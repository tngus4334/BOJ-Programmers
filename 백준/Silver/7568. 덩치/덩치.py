n = int(input())
kgcm_list = []
for i in range(n):
    kg, cm = map(int,input().split())
    kgcm_list.append((kg,cm))

for i in range(n):
    cnt = 1
    for j in range(n):
        if kgcm_list[i][0] < kgcm_list[j][0] and kgcm_list[i][1] < kgcm_list[j][1]:
            cnt += 1
    print(cnt,end=' ')
