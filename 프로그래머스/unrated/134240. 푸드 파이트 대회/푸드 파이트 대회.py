def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if food[i] == 1:
            pass
        else :
            for _ in range(food[i]//2):
                answer += str(i)
    answer += '0'
    answer += answer[:-1][::-1]
    return answer