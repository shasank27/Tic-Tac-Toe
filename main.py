lis = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def line():
    print("   |     |")


def inline(lis, ind):
    print(" {} |  {}  | {}".format(lis[ind], lis[ind + 1], lis[ind + 2]))


def stline():
    print("---------------")


def printmat():
    for i in range(0, 9, 3):
        line()
        inline(lis, i)
        if i != 6:
            stline()


printmat()


def check():
    for inwhi in range(0, 9, 3):
        if (lis[inwhi] == lis[inwhi + 1]) and (lis[inwhi + 2] == lis[inwhi + 1]):
            if lis[inwhi] == a:
                print("PLAYER 1  WINS")
                return 1
            else:
                print("PLAYER 2  WINS")
                return 1
    for inwhi in range(0, 3):
        if (lis[inwhi] == lis[inwhi + 3]) and (lis[inwhi + 3] == lis[inwhi + 6]):
            if lis[inwhi] == a:
                print("PLAYER 1  WINS")
                return 1
            else:
                print("PLAYER 2  WINS")
                return 1
    if (lis[0] == lis[4]) and (lis[4] == lis[8]):
        if lis[0] == a:
            print("PLAYER 1  WINS")
            return 1
        else:
            print("PLAYER 2  WINS")
            return 1
    if (lis[2] == lis[4]) and (lis[4] == lis[6]):
        if lis[2] == a:
            print("PLAYER 1  WINS")
            return 1
        else:
            print("PLAYER 2  WINS")
            return 1
    return 0


a = input("Player 1 choose your mark 'X' or '0' : ")
b = None
if a == 'X':
    b = '0'
else:
    b = 'X'
print("Mark for Player1 is {}".format(a))
print("Mark for Player2 is {}".format(b))
print("Rules : First Player1 will choose a number which will be replaced ")
print("by his/her mark then Player2 will choose a number which will be ")
print("replaced by his/her mark and it'll continue subsequently")
whi = 0
while whi < 9:
    if whi % 2 == 0:
        pos = int(input("Player1 choose your position (1-9) : ")) - 1
        if pos<0:
            print("Enter between 1-9.")
            whi -= 1
        elif pos>=9:
            print("Enter between 1-9.")
            whi -= 1
        else:
            if (lis[pos]) == b:
                print("Enter positions that are not  used")
                whi -= 1
            else:
                lis[pos] = a

    else:
        pos = int(input("Player2 choose your position (1-9) : ")) - 1
        if pos < 0:
            print("Enter between 1-9.")
            whi -= 1
        elif pos >= 9:
            print("Enter between 1-9.")
            whi -= 1
        else:
            if (lis[pos]) == a:
                print("Enter positions that are not  used")
                whi -= 1
            else:
                lis[pos] = b
    printmat()
    check1 = check()
    if check1 == 1:
        break
    whi += 1

if check1 == 0 and whi == 9:
    print("No one wins")
