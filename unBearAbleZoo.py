#Un-bear-able Zoo
#https://open.kattis.com/problems/zoo

def display(dictData, n):
    print("List {}:".format(n))
    for key in sorted(dictData.keys()):
        print("{} | {}".format(key, dictData[key]))

counter = 0
while True:
    counter += 1
    n = int(input())
    animals = {}
    if n == 0: break
    for _ in range(n):
        s = input().split()
        if s[-1].lower() not in animals.keys():
            animals.update({s[-1].lower():1})
        else:
            animals[s[-1].lower()] += 1
    display(animals, counter)
