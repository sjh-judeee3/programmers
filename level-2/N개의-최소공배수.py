def gcd(a, b):
    if a > b:
        a, b = b, a
    while b%a != 0:
        b, a = a, b%a
    return a

def solution(arr):
    answer = 1
    arr = sorted(arr)

    #두 개의 수끼리 최소공배수를 구하고 최소공배수와 다음 수의 최소공배수 구하기
    for i in range(1, len(arr)):
        gcd_num = gcd(arr[i-1], arr[i])
        answer = int(arr[i-1] * arr[i] / gcd_num)
        arr[i] = answer

    return answer