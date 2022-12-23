x, y, w, s = map(int, input().split())

way_1 = (x+y) * w

if (x + y) % 2 == 0:
    way_2 = max(x, y) * s
else:
    way_2 = (max(x, y) - 1) * s + w

way_3 = (min(x, y) * s) + (abs(x-y) * w)

print(min(way_1, way_2, way_3))