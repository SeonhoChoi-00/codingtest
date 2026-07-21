def solution(s):
    arr = []
    for i in s:
        if i == "(":
            arr.append(i)
        else:
            if len(arr) > 0 and arr.pop() == "(":
                pass
            else:
                return False
    if arr:
        return False
    return True