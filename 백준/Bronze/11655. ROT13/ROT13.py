ROT13 = list(input())

for i in range(len(ROT13)):
    if (65 <= ord(ROT13[i]) <= 90) or (97 <= ord(ROT13[i]) <= 122):
        if (65 <= ord(ROT13[i]) <= 77) or (97 <= ord(ROT13[i]) <= 109):
            ROT13[i] = chr(ord(ROT13[i]) + 13)

        else:
            ROT13[i] = chr(ord(ROT13[i]) - 13)


print(''.join(ROT13))