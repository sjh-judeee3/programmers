def solution(s):
    cnt = 1
    answer = len(s)
    while cnt < len(s):
        prevword = None
        prevcnt = 0
        tempans = 0
        for i in range(0, len(s)//cnt+1):
            curword = s[i*cnt:min((i+1)*cnt, len(s))]
            templen = min((i+1)*cnt, len(s)) - i*cnt
            if prevword == curword:
                prevcnt += 1
            else:
                if prevcnt != 0:
                    tempans += len(str(prevcnt+1))
                tempans += templen
                prevword = curword
                prevcnt = 0
        answer = min(tempans, answer)
        cnt += 1
    
    return answer