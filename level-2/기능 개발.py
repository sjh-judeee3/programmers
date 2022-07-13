def solution(progresses, speeds):
    ptr = 0
    answer = []
    while ptr < len(progresses):
        tempans = 0
        for i in range(len(speeds)):
            progresses[i] = progresses[i] + speeds[i]
        while ptr < len(progresses) and progresses[ptr] >= 100:
            tempans += 1
            ptr += 1
        if tempans != 0:
            answer.append(tempans)
    return answer