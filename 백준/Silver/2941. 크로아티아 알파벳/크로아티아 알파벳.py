s = input()
t = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in t:
    s = s.replace(i, 'o')
print(len(s))
