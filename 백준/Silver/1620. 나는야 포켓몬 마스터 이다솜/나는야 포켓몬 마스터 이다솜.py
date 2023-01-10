import sys
input = sys.stdin.readline

n, k = map(int,input().split())

code = {}
pokemon_name = {}

for i in range(1,n+1):
    pokemon = input().rstrip()
    code[i] = pokemon
    pokemon_name[pokemon] = i

for _ in range(k):
    answer = input().rstrip()

    if answer.isdigit():
        print(code.get(int(answer)))
    else:
        print(pokemon_name.get(answer))