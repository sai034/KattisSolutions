#	Cudoviste
#https://open.kattis.com/problems/cudoviste

def isWith(x, y):
    return 0 <= x < w and 0 <= y < h

def get(map, x, y):
    if isWith(x, y):
        return map[y][x]
    else:
        return None


s = input().split()
h = int(s[0])
w = int(s[1])
tH = 2
tW = 2

map = []
for _ in range(h):
    row = input()
    map.append(row)

options = {}
for row in range(h):
    for column in range(w):
        numberOfCars = 0
        wasBlocked = False
        for truckY in range(tH):
            for truckX in range(tW):
                x = column + truckX
                y = row + truckY
                entry = get(map, x, y)
                if entry == None or entry == "#":
                    wasBlocked = True
                elif entry == "X":
                    numberOfCars += 1
        if not wasBlocked:
            options[numberOfCars] = options.get(numberOfCars, 0) + 1
for numberOfCars in range(5):
    numberOfPossibilities = options.get(numberOfCars, 0)
