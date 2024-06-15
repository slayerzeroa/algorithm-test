from copy import deepcopy

while True:
    try:
        N = int(input())

        result = []
        for i in range(N+1):
            if i == 0:
                result.append('-')
            else:
                image = deepcopy(result)
                result.extend([' ' for _ in range(len(result))])
                result.extend(image)

        print(''.join(result))
    except:
        break