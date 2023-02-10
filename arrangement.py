#Arrangement
#https://open.kattis.com/problems/upprodun

import itertools
print((lambda m, n: (lambda c, d: "\n".join(itertools.chain(('*' * (c+1) for i in range(d)), ('*' * c for i in range(m-d)))))(*divmod(n, m)))(int(input()), int(input())))
