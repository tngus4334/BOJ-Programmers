a,b = map(int,input().split())


if a <= b:
    a_sum = a * (a - 1) // 2
    b_sum = ((b + 1) * b) // 2
    print(b_sum-a_sum)
else:
    a_sum = ((a + 1) * a) // 2
    b_sum = b * (b - 1) // 2
    print(a_sum - b_sum)