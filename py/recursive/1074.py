N, r, c = list(map(int, input().split()))


def search(N, r, c):
    if N==0:
        return 0
    return (2*(r%2)+(c%2) + 4*search(N-1, r//2, c//2))

print(search(N, r, c))