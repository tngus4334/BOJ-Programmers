n, m = map(str,input().split())
eight = 0
if len(n) != len(m):
    print(0)

else:
    for i in range(len(n)):
        if n[i] == m[i]:
            if n[i] == '8':
                eight += 1
        else:
            break
    print(eight)