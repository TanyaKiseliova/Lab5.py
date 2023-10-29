import math

def task1():
    a=0.3
    b=-21.17
    y=(a+1.5)**(1./3)+(a-b)**8-b/(math.asin(math.fabs(a)**2))
    print(y)

def task2():
    pass

def task3():
    pass

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def inputInt(description):
    str = input(description)
    while not isInt(str):
        print("Incorrect input. Input only numbers")
        str = input()
    return int(str)

def main():

    while True:
        print("1.task 1")
        print("2.task 2")
        print("3.task 3")
        print("4.exit")

        ch=inputInt("Choose: ")

        if ch==1:
            task1()
        elif ch==2:
            task2()
        elif ch==3:
            task3()
        elif ch==4:
            break
        else:
            print("Incorrect input")


main()