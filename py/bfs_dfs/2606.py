from collections import deque

N = int(input())
K = int(input())

graph = {i:[] for i in range(N+1)}


for _ in range(K):
    f, l = map(int, input().split())
    graph[f].append(l)
    graph[l].append(f)
# print("그래프")
# print(graph)

def bfs(graph, start):
    
    visited = [False for i in range(N+1)]
    q = deque()
    # deque에 start 방문 처리
    q.append(start)
    
    while q:
        p = q.popleft()
        # print("p=",p)
        # print("q=",q)
        if visited[p] == False:
            visited[p] = True
            q.extend(graph[p])
    
    count = 0
    # print("visited:", visited)
    for i in visited:
        if i == True:
            count+=1
    return (count-1)

# print("결과값")
print(bfs(graph, 1))