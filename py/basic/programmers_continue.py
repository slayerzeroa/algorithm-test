# # 프로그래머스 연속된 부분 수열의 합

# def solution(sequence, k):
#     answer = []

#     n=1  
#     while n <= len(sequence):
#         for idx in range(len(sequence)-n+1):
#             part = sequence[idx:idx+n]
#             result = sum(part)
#             if result == k:
#                 answer.append(idx)
#                 answer.append(idx+n-1)
#                 return answer
#         n+=1




# def solution(sequence, k):
#     answer = []

#     n=1  
#     while n <= len(sequence):
#         for idx in range(len(sequence)-n+1, -1, -1):
#             part = sequence[idx:idx+n]
#             result = sum(part)
#             if result == k:
#                 answer.append([idx, idx+n-1])
#         if len(answer)!=0:
#             return answer[-1]
#         n+=1


# def solution(sequence, k):
#     answer = []
    
#     start = 0
#     end = 1
    
#     while start != len(sequence):
#         result = sequence[start:end]
#         if sum(result) < k:
#             end += 1
#         elif sum(result) > k:
#             start += 1
#         else:
#             return([start, end-1])
    
#     return answer


def solution(sequence, k):
    answer = []
    
    start = len(sequence) - 1
    end = len(sequence)
    
    while start != -1:
        result = sequence[start:end]
        if sum(result) < k:
            start -= 1
        elif sum(result) > k:
            end -= 1
            if start == end:
                start = end - 1
        else:
            answer.append([start, end-1])
            start -= 1
            end -= 1
    answer.reverse()
    length_list = []
    for i in answer:
        length_list.append(i[1]-i[0])
    min_idx = length_list.index(min(length_list))
    return answer[min_idx]

sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5

print(solution(sequence, k))