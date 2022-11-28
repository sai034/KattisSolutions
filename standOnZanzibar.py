#	Stand on Zanzibar
#https://open.kattis.com/problems/zanzibar

import sys
noc = 0
is_done = False
for i in sys.stdin:
    if not is_done:
        noc = (int)(i.split()[0])
        is_done = True
    elif not noc == 0:
        cases = []
        inputCases = i.split()
        for case in inputCases:
            cases.append((int)(case))
        old_case = cases[0]
        not_born = 0
        for case in cases[1:]:
            if (case == 0):
                break
            else:
                if (case - old_case*2 > 0):
                    not_born += case - old_case*2
                old_case = case
        print(not_born)
        noc -= 1
    else:
        quit()
