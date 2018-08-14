from random import randint,choice
# from evel import calc
loop = True
import evel

while loop :
    x = randint(1,10)
    y = randint(1,10)
    op = ['+','-','*','/']
    error = [-1,0,1]

    op_rand = choice(op)
    error_rand = choice(error)

    res = evel.calc(x,y,op_rand)

    display_res = res + error_rand

    print("* "*20)
    print("{} {} {} = {}".format(x,op_rand,y,display_res))
    print("* "*20)

    ans = input("(Y/N)? ").upper()

    if error_rand == 0:
        if ans == "Y":
            print("Yay")
        elif ans == "N":
            print("wrong")
            loop = False
    elif error_rand != 0:
        if ans == "Y":
            print("Wrong")
            loop = False
        elif ans =="N":
            print("Yay")
            