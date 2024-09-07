# # Programmers LV2 - 뒤에 있는 큰 수 찾기
# def solution(numbers):
#     answer = []
#     N = len(numbers)
#     for idx, i in enumerate(numbers):
#         if (idx == N-1):
#             answer.append(-1)
#             break
#         for j in range(idx, N):
#             if numbers[j] > numbers[idx]:
#                 answer.append(numbers[j])
#                 break
#             else:
#                 if (j == N-1):
#                     answer.append(-1)
#                     break
#                 else:
#                     pass
#     return answer

# def solution(numbers):
#     answer = []
#     N = len(numbers)
#     last = 0
#     test = []
#     for i in range(N):
#         popping = numbers.pop()
#         if len(test)==0:
#             test.append(-1)
#         elif last > popping:
#             test.append(last)
#         else:
#             for idx, j in enumerate(reversed(test)):
#                 if j > popping:
#                     test.append(j)
#                     break
#                 elif idx == len(test)-1:
#                     test.append(-1)
#         last = popping
#     test.reverse()
#     answer = test
#     return answer



# def solution(numbers):
#     answer = []
#     N = len(numbers)
#     last = 0
#     test = []
#     biggest = 0
#     for i in range(N):
#         popping = numbers.pop()
#         if len(test)==0:
#             test.append(-1)
#         elif last > popping:
#             test.append(last)
#         else:
#             if biggest > popping:
#                 for idx, j in enumerate(reversed(test)):
#                     if j > popping:
#                         test.append(j)
#                         break
#                     elif idx == len(test)-1:
#                         test.append(-1)
#             else:
#                 test.append(-1)
#         if test[i] > biggest:
#             biggest = test[i]
#         last = popping
#     test.reverse()
#     answer = test
#     return answer