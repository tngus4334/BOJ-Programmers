s = list(map(str, input()))
t = list(map(str, input()))

while len(s) != len(t):
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]

if s == t:
    print(1)
else:
    print(0)