def solution(numer1, denom1, numer2, denom2):
    answer = []
    n = numer1 * denom2 + numer2 * denom1
    d = denom1 * denom2
    a = max(n, d)
    b = min(n, d)
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    n /= b
    d /= b
    answer.extend([n, d])
    return answer