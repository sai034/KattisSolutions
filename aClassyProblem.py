#	A Classy Problem
#https://open.kattis.com/problems/classy

[print('\n'.join(map(lambda w: w[1], sorted([tuple((lambda r: [''.join((lambda l: l + ['1' for i in range(10 - len(l))])(list(map(lambda o: '0' if o[0] == 'u' else '1' if o[0] == 'm' else '2', reversed(r[1].split("-")))))), r[0][:-1]])(input().split())) for i in range(int(input()))]))) + '\n' + ('=' * 30)) for p in range(int(input()))]
