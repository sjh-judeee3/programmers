def solution(array):
    answer = 0
    
    for num in array:
        num = list(str(num))
        answer = answer + num.count('7')
    
    return answer