import math
import numpy as np
def task1_1():
    a=0.3
    b=-21.17
    y=(a+1.5)**(1./3)+(a-b)**8-b/(math.asin(math.fabs(a)**2))
    print(y)

def task1_2():
    X=np.array([
        [1,12,61],
        [1,13,63],
        [1,14,65],
        [1,15,63],
        [1,16,64],
        [1,17,65],
        [1,18,67],
        [1,19,69],
        [1,20,70],
        [1,21,71],
        [1,22,73],
        [1,23,80]
    ])

    Y=np.array([
        13.6,
        14.0,
        14.3,
        14.5,
        14.8,
        15.1,
        15.3,
        16.9,
        17.1,
        17.8,
        18.1,
        18.5
    ])

    X_trans=X.T
    X_trans_X=X_trans.dot(X)
    X_trans_X_revers=np.linalg.inv(X_trans_X)
    X_trans_Y=X_trans.dot(Y)
    A=X_trans_X_revers.dot(X_trans_Y)
    print("Vector for estimating regression equations= ", A)

    Y_exam=X.dot(A)
    print("Y = ", Y)
    print("Y for examination = ", Y_exam)

    if np.allclose(Y, Y_exam, 0.1):
        print("The chech was successful, the values are approximately equal")
    else:
        print("The chech wasn't successful, the values aren't approximately equal")
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
        print("1.task 1.1 the equation (math)")
        print("2.task 1.2 matrix (numpy)")
        print("3.task 2")
        print("4.task 3")
        print("5.exit")

        ch=inputInt("Choose: ")

        if ch==1:
            task1_1()
        elif ch==2:
            task1_2()
        elif ch==3:
            task2()
        elif ch==4:
           task3()
        elif ch == 5:
            break
        else:
            print("Incorrect input")


main()