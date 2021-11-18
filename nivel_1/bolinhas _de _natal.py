b = int(input())
g = int(input())


r = g/ 2

if (r <= b):
    print("Amelia tem todas bolinhas!")

else:
    print("Faltam {} bolinha(s)".format(int(r - b)))