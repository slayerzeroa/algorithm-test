def solution(inputArray):
    longest_len = 0
    answer = []
    for item in inputArray:
        if len(item) > longest_len:
            answer = []
            longest_len = len(item)
            answer.append(item)
        elif len(item) == longest_len:
            answer.append(item)
        else:
            pass
    return answer