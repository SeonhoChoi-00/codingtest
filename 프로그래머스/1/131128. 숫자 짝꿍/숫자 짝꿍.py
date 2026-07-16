def solution(X, Y):
    count_x = [0] * 10
    count_y = [0] * 10
    Min = [0] * 10
    res = []
    
    for i in X:
        count_x[int(i)] += 1
    for i in Y:
        count_y[int(i)] += 1
    
    for i in range(10):
        Min[i] = min(count_x[i], count_y[i])
    
    for i in range(9, -1, -1):
        cnt = Min[i]
        if cnt > 0:
            res.append(str(i)*cnt)
    
    answer = ''.join(res)
    
    if not res:
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        return answer