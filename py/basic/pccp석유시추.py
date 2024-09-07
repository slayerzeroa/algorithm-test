land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]

def solution(land):
    answer = 0
    visited = [[0 for i in range(len(land[0]))] for j in range(len(land))]
    result = [[0 for i in range(len(land[0]))] for j in range(len(land))]
    area = {}
    n = len(land[0])
    m = len(land)
    global count
    count = 0

    def dfs(x, y, initial):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        global count
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if visited[y][x] == 0:
            visited[y][x] = 1
            if (land[y][x] == 1):
                result[y][x] = initial
                count += 1
                area[initial] = count
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    dfs(nx, ny, initial)

    initial = 100
    for i in range(len(land[0])):
        for j in range(len(land)):
            count = 0
            dfs(i, j, initial)
            initial += 1
    area[0] = 0
    submit = [[] for i in range(len(result[0]))]
    for j in result:
        for idx, i in enumerate(j):
            submit[idx].append(i)

    result = []
    for i in submit:
        result.append(list(set(i)))

    answer_list = []

    for r in result:
        point = 0
        for i in r:
            point += area[i]
        answer_list.append(point)

    answer = max(answer_list)
    return answer 



from collections import deque
def solution(land):
    answer = 0
    visited = [[0 for i in range(len(land[0]))] for j in range(len(land))]
    result = [[0 for i in range(len(land[0]))] for j in range(len(land))]
    area = {}
    n = len(land[0])
    m = len(land)
    global count
    count = 0

    def bfs(x, y, initial):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        global count

        q = deque()
        q.append((y, x))

        while q:
            y, x = q.popleft()
            count += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if (visited[ny][nx] == 0) & (land[ny][nx] == 1):
                    result[ny][nx] = initial
                    area[initial] = count
                    visited[ny][nx] = 1
                    q.append((ny, nx))

    initial = 100
    for i in range(len(land[0])):
        for j in range(len(land)):
            count = 0
            bfs(i, j, initial)
            initial += 1
    area[0] = 0
    submit = [[] for i in range(len(result[0]))]
    for j in result:
        for idx, i in enumerate(j):
            submit[idx].append(i)

    result = []
    for i in submit:
        result.append(list(set(i)))

    answer_list = []

    for r in result:
        point = 0
        for i in r:
            point += area[i]
        answer_list.append(point)

    answer = max(answer_list)
    return answer


print(solution(land))