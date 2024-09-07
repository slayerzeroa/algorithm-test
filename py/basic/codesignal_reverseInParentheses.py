def solution(inputString):
    inputList = list(inputString)
    while ('(' in inputList) or (')' in inputList):
        start = 0
        end = 0
        while end < len(inputList):
            if inputList[end] == '(':
                start = end
            elif inputList[end] == ')':
                if end - start == 1:
                    inputList.pop(end)
                    inputList.pop(start)
                else:
                    change_term = inputList[start+1:end]
                    change_term = change_term[::-1]
                    inputList[start:end+1] = change_term
                    break

            end += 1
    return ''.join(inputList)