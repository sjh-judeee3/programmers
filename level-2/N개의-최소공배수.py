def gcd(a, b):
    if a > b:
        a, b = b, a
    while b%a != 0:
        b, a = a, b%a
    return a

def solution(arr):
    
    arr = sorted(arr)

    gcd = 1

    #gcd 구하기
    for i in range(1, arr[0]+1):
        flag = True
        
        for num in arr:
            if num % i != 0:
                flag = False
                break
                
        if flag == True and i > gcd:
            gcd = i
            
    answer = 1
    for num in arr:
        answer = answer * num
    answer = int(answer // gcd ** (len(arr)-1))

    return answer

print(solution([3, 4, 9, 16]))
