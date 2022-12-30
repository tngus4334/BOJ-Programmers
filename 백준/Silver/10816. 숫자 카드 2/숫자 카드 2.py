n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_card = {}
for i in n_list:
    if i in n_card:
        n_card[i] += 1
    else:
        n_card[i] = 1

for j in m_list:
    result = n_card.get(j)
    if result != None:
        print(result, end=" ")
    else:
        print(0, end=" ")
