#	Luhn's Checksum Algorithm
#https://open.kattis.com/problems/luhnchecksum

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10
N=int(input())
for i in range(N):
    p=str(input())
    if luhn_checksum(p)==0:
        print("PASS")
    else:
        print("FAIL")
