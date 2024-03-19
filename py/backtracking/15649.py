# # 백준 15649
# N, M = map(int, input().split())
# result = []
# visited = [0 for _ in range(N+1)]

# def dfs(n, line):
#     # 종료조건(n에 관한) 처리 + 정답 처리
#     if n==M:
#         result.append(line)
#         return

#     # 하부단계 (함수) 호출
#     for j in range(1, N+1):
#         if visited[j]==0:
#             visited[j]=1
#             dfs(n+1, line+[j])
#             visited[j]=0


# dfs(0, [])

# for line in result:
#     print(*line)


N, M = map(int, input().split())
