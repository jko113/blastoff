from time import sleep

def blast(top):

    while top >= 0:
        sleep(1)
        if top == 0:
            print("You've gotten to....", end='')
        print(top)
        top -= 1