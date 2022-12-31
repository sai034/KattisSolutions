#	Radio Commercials
#https://open.kattis.com/problems/commercials

def max_subarray(numbers):
    best_sum = 0
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
n,p = map(int,input().split())
print(max_subarray(list(map(lambda z: int(z) - p, input().split()))))
