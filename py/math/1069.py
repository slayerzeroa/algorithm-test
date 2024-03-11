#백준 1069번


x, y, d, t = map(int, input().split())

dist = (x**2 + y**2)**(0.5)


def timebydist(dist, d, t):
    time = 0
    while dist >= d:
        dist -= d
        time += t
    return time + abs(dist)

def overbydist(dist, d, t):
    time = 0
    while abs(dist - d) < d:
        dist -= d
        time += t
    return time + abs(dist)

def zigzag(dist, d, t):
    if dist < d:
        return 2 * t
    else:
        return ((dist // d + 1) * t)
    
def justwalk(dist):
    return dist

route1 = timebydist(dist, d, t)
route2 = overbydist(dist,d, t)
route3 = zigzag(dist, d, t)
route4 = justwalk(dist)

print(min([route1, route2, route3, route4]))