def solution(k, m, score):
    n = len(score) // m
    score.sort(reverse=True)
    res = 0
    i = 0
    while i < m * n:
        res += score[i + m - 1] * m
        if i != m * (n - 1) - 1:
            i += m
    return res