import itertools
mini_list = []
for i in range(9):
    mini_list.append(int(input()))

mini_combi = itertools.combinations(mini_list,7)

mini_combi_10 = []
for i in mini_combi:
    if sum(i) == 100:
        mini_combi_10.append(i)
for k in range(7):
    print(mini_combi_10[0][k])