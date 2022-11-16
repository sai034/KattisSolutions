#	Left Beehind
#https://open.kattis.com/problems/leftbeehind

so,sw=list(map(int,input().split()))
while so!=0 or sw!=0:
    if so+sw==13:
        print("Never speak again.")
    elif so>sw:
        print("To the convention.")
    elif so==sw:
        print("Undecided.")
    elif so<sw:
        print("Left beehind.")
    so,sw=list(map(int,input().split()))
