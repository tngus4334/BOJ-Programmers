mushroom_list = []
mushroom_score = 0
for _ in range(10):
    mushroom_list.append(int(input()))

for eat in mushroom_list:
    mushroom_score += eat
    if mushroom_score >= 100:
        if mushroom_score - 100 > 100 - (mushroom_score - eat):
            mushroom_score -= eat
        break
print(mushroom_score)