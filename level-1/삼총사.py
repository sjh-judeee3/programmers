def solution(number):
    number = sorted(number)
    answer = 0
    total = 0
    
    for i in range(len(number)):
        for j in range(len(number)):
            for k in range(len(number)):
                if (i != j) and (j != k) and (k != i) and (number[i] + number[j] + number[k] == 0):
                    print(number[i], number[j], number[k])
                    total = total + 1
    
    answer = total/6
    return answer
