ndmy_list = []
for _ in range(int(input())):
    name, d, m, y = input().split()
    ndmy_list.append([name, int(d), int(m), int(y)])
ndmy_list.sort(key=lambda x : (x[3], x[2], x[1]))

print(ndmy_list[-1][0])
print(ndmy_list[0][0])