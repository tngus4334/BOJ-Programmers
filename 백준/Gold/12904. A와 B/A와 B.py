S = list(input())
T = list(input())

while len(S) != len(T):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)