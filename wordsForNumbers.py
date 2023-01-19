#	Words for Numbers
#https://open.kattis.com/problems/wordsfornumbers

import fileinput
ans = {}
ans[0] = "zero"
ans[1] = "one"
ans[2] = "two"
ans[3] = "three"
ans[4] = "four"
ans[5] = "five"
ans[6] = "six"
ans[7] = "seven"
ans[8] = "eight"
ans[9] = "nine"
ans[10] = "ten"
ans[11] = "eleven"
ans[12] = "twelve"
ans[13] = "thirteen"
ans[14] = "fourteen"
ans[15] = "fifteen"
ans[16] = "sixteen"
ans[17] = "seventeen"
ans[18] = "eighteen"
ans[19] = "nineteen"
ans[20] = "twenty"
ans[30] = "thirty"
ans[40] = "forty"
ans[50] = "fifty"
ans[60] = "sixty"
ans[70] = "seventy"
ans[80] = "eighty"
ans[90] = "ninety"
for j in range(20, 100, 10):
    for i in range(1, 10):
        ans[j + i] = ans[j] + '-' + ans[i]
for line in fileinput.input():
    for idx, word in enumerate(line.split()):
        try:
            output = ans[int(word)]
            if idx == 0:
                output = output[0].upper() + output[1:]
            print(output, end=' ')
        except:
            print(word, end=' ')
    print()
