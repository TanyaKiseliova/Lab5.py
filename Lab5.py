import math
import numpy as np
import matplotlib.pyplot as plt

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

def task3_1():
    t_start=2
    t_end=3
    delta_t=0.05

    t_val=np.arange(t_start, t_end+delta_t, delta_t)
    s_val=[]

    for t in t_val:
        s=math.log(math.fabs(1.3+t))-math.exp(t)
        s_val.append(s)

    for t, s in zip(t_val, s_val):
        print(f"t = {t:.2f}, s = {s:.2f}")

    max_s=max(s_val)
    min_s=min(s_val)
    mean_s=np.mean(s_val)

    print(f"Max value: {max_s:.2f}")
    print(f"Min value: {min_s:.2f}")
    print(f"Average value: {mean_s:.2f}")

    sorted_s_values=sorted(s_val)

    plt.figure(figsize=(10,6))
    plt.plot(t_val, s_val, label="f(t)", marker='o')
    plt.axhline(mean_s, color='red', linestyle='--', label="Average value")
    plt.xlabel("t")
    plt.ylabel("f(t)")
    plt.title("Graph of a function f(t)")
    plt.grid(True)
    plt.legend()

    plt.show()

def task3_2():
    fig, axes= plt.subplots(2,3, figsize=(15, 10))

    x=np.linspace(4, 20, 10)
    y=np.linspace(4, 20, 10)
    X, Y=np.meshgrid(x,y)

    Z1=X**0.25+Y**0.25
    axes[0, 0].contour(X, Y, Z1, levels=20, colors='k')
    axes[0, 0].set_title("z = x^0.25+y^0.25")
    axes[0,0].set_xlabel('X')
    axes[0,0].set_ylabel('Y')

    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)

    Z2 = X ** 2 - Y ** 2
    axes[0, 1].contour(X, Y, Z2, levels=20, colors='k')
    axes[0, 1].set_title('z = x^2 - y^2')
    axes[0, 1].set_xlabel('X')
    axes[0, 1].set_ylabel('Y')

    Z3 = 2*X+3*Y
    axes[0, 2].contour(X, Y, Z3, levels=20, colors='k')
    axes[0, 2].set_title('z = 2x + 3y')
    axes[0, 2].set_xlabel('X')
    axes[0, 2].set_ylabel('Y')

    Z4 = X ** 2 + Y ** 2
    axes[1, 0].contour(X, Y, Z4, levels=20, colors='k')
    axes[1, 0].set_title('z = x^2 + y^2')
    axes[1, 0].set_xlabel('X')
    axes[1, 0].set_ylabel('Y')

    Z5 = 2+2*X+2*Y-X**2-Y**2
    axes[1, 1].contour(X, Y, Z5, levels=20, colors='k')
    axes[1, 1].set_title('z = 2 + 2x + 2y - x^2 - y^2')
    axes[1, 1].set_xlabel('X')
    axes[1, 1].set_ylabel('Y')

    axes[1,2].axis('off')

    plt.tight_layout()
    plt.show()

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
        print("4.task 3_1 (matplotlib)")
        print("5.task 3_2 (matplotlib several graph)")
        print("6.exit")

        ch=inputInt("Choose: ")

        if ch==1:
            task1_1()
        elif ch==2:
            task1_2()
        elif ch==3:
            task2()
        elif ch==4:
           task3_1()
        elif ch == 5:
           task3_2()
        elif ch == 6:
            break
        else:
            print("Incorrect input")


main()